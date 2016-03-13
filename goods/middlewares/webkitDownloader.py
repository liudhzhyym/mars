import sys
import os
os.environ['DISPLAY'] = ':0'
sys.path.append("/home/ubuntu/opbin/liudonghai/spder/goods")
from scrapy.http import Request, FormRequest, HtmlResponse
 
import gtk
import webkit
import jswebkit
import settings

class WebkitDownloader(object):
    def process_request(self, request, spider):
	print "11111111111111111"
        if spider.name in settings.WEBKIT_DOWNLOADER:
	    print "22222222222222222"
            if(type(request) is not FormRequest):
	    	print "33333333333"
                webview = webkit.WebView()
                webview.connect('load-finished', lambda v, f: gtk.main_quit())
                webview.load_uri(request.url)
                gtk.main()
                js = jswebkit.JSContext(webview.get_main_frame().get_global_context())
                rendered_body = str(js.EvaluateScript('document.body.innerHTML'))
		print "body = ",renderedBody
                return HtmlResponse(request.url, body=rendered_body)

            
