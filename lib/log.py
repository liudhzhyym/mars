#! python
# coding: utf8

import os
import time
import datetime
import traceback
import inspect
import random
import UserDict
import codecs
import errno
import fcntl
import sys


class LogVariable(object):
  def __init__(self, init_value, callback=None, callback_args=None, cached=True):
    self.init_value = init_value
    self.value = None
    self.callback = callback
    self.callback_args = callback_args
    self.cached = cached

  def get(self):
    if self.cached:
      if self.value is None:
        if self.callback is None:
          self.value = self.init_value
        else:
          if self.callback_args is None:
            self.value = self.callback()
          else:
            self.value = self.callback(self.callback_args)
    else:
      if self.callback is None:
        self.value = self.init_value
      else:
        if self.callback_args is None:
          self.value = self.callback()
        else:
          self.value = self.callback(self.callback_args)
    return self.value
          

class Log(object):
  ERROR = 0x01
  INFO = 0x02
  NOTICE = 0x03
  
  LEVELS = {
    0x01: 'ERROR',
    0x02: 'INFO',
    0x03: 'NOTICE'
  }

  def __init__(self, log_file):
    self.encoding = 'utf8'
    self.log_file = log_file
    self.log_filename = os.path.basename(self.log_file)
    self.log_dir = os.path.dirname(self.log_file)
    self.fp = None
    self.parse_logfile()
    self.open_filename = self.open_filename_gen()
    self.open_file()
    self.fetch_logid()
    self.headers = UserDict.UserDict()
    self.notice_headers = UserDict.UserDict()
    self.once_headers = UserDict.UserDict()
    self.lock_file = os.path.join(self.log_dir, '%s.lock' % self.log_fileprefix)
    self.lock_fd = os.open(self.lock_file, os.O_RDWR | os.O_CREAT)

  def __del__(self):
    self.release_lock()
    try:
      os.close(self.lock_fd)
    except:
      pass
    self.close_file()

  def renew(self):
    self.headers.clear()
    self.notice_headers.clear()
    self.fetch_logid()

  def acquire_lock(self, blocking=True):
    if blocking:
      fcntl.flock(self.lock_fd, fcntl.LOCK_EX)
      return True
    else:
      try:
        fcntl.flock(self.lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
        return True
      except IOError as e:
        if e.errno == errno.EACCES or e.errno == errno.EAGAIN:
          return False
        else:
          raise e

  def release_lock(self):
    try:
      fcntl.flock(self.lock_fd, fcntl.LOCK_UN)
    except IOError as e:
      pass

  def fetch_logid(self):
    if 'LOGID' in os.environ:
      self.log_id = os.environ['LOGID']
    else:
      now = datetime.datetime.now()
      ss = now.minute * 60 + now.second
      ms = now.microsecond / 1000
      sr = random.randint(0,999)
      self.log_id = '%04d%03d%03d' % (ss, ms, sr)
      os.environ['LOGID'] = self.log_id
    return self.log_id

  def get_logid(self):
    return self.log_id
     
  def parse_logfile(self):
    a = self.log_filename.rsplit('.', 1)
    if len(a) < 2:
      self.rotate = False
    else:
      self.ts_suffix = a[1]
      self.log_fileprefix = a[0]
      self.rotate = True
    
  def open_filename_gen(self):
    if self.rotate:
      ret = os.path.join(self.log_dir, '%s.%s' % (self.log_fileprefix, time.strftime(self.ts_suffix)))
    else:
      ret = self.log_filename
    return ret 

  def open_file(self):
    self.close_file()
    self.fp = open(self.open_filename, 'a')
  
  def close_file(self):
    if hasattr(self.fp, 'close'):
      self.fp.close()

  def _set_header(self, d, k, init_value, callback=None, callback_args=None, cached=True):
    v = d.get(k, LogVariable(init_value, callback, callback_args, cached))
    v.value = None
    d[k] = v

  def set_header(self, k, init_value, **kwargs):
    self._set_header(self.headers, k, init_value, **kwargs)

  def set_notice(self, k, init_value, **kwargs):
    self._set_header(self.notice_headers, k, init_value, **kwargs)

  def set_once(self, k, init_value, **kwargs):
    self._set_header(self.once_headers, k, init_value, **kwargs)

  def get_caller(self):
    fm = inspect.currentframe()
    fm_info = inspect.getframeinfo(fm)
    curr_filename = fm_info.filename
    while fm_info.filename == curr_filename:
      fm = fm.f_back
      fm_info = inspect.getframeinfo(fm)
    
    return (fm, fm_info)

  def get_generic_header(self, level):
    (caller, caller_info) = self.get_caller()
    ret = '[%s] [%s] *%d* [%s:%d %s] logid[%s]' % (
      time.strftime('%Y-%m-%d %H:%M:%S'), self.LEVELS[level], os.getpid(), os.path.basename(caller_info.filename), caller_info.lineno, caller_info.function, self.log_id
    )
    return ret

  def get_header(self, level):
    headers = [self.get_generic_header(level)]
    for (k, v) in self.headers.items() + self.once_headers.items():
      headers.append('%s[%s]' % (k, v.get()))
      
    if level == self.NOTICE:
      for (k, v) in self.notice_headers.items():
        headers.append('%s[%s]' % (k, v.get()))
      
    return ' '.join(headers)

  def _write_log(self, level, msg, fp):
    if isinstance(msg, unicode):
      msg = codecs.encode(msg, self.encoding, 'replace')
    else:
      msg = str(msg)
    self.acquire_lock(True)
    fp.write('%s %s\n' % (self.get_header(level), msg.replace('\n', '\\n')))
    fp.flush()
    self.release_lock()

  def std_log(self, level, msg):
    self._write_log(level, msg, sys.stderr)

  def write_log(self, level, msg):
    if self.open_filename_gen() != self.open_filename:
      self.open_filename = self.open_filename_gen()
      self.open_file()

    self._write_log(level, msg, self.fp)
    self.once_headers.clear()
  
  def notice(self, msg):
    self.write_log(self.NOTICE, msg)

    
    
