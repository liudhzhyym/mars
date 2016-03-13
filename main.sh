#!/bin/bash

# 1 获取所有网站列表
# 2 遍历所有网站列表，建立对应的文件夹，克隆最新代码
# 3 找出本机上需要执行的任务，并发启动抓取脚本
# 4 抓取网站，上传数据/图片

FILE_PATH=`readlink -f $0`

CUR_DIR=`dirname $FILE_PATH`
FILE=`basename $FILE_PATH`
LOG_DIR=$CUR_DIR/log/main/
CURRENT_TIME=`date +%Y%m%d%H`
LOG_FILE="${LOG_DIR}/main.log.${CURRENT_TIME}"
DEPLOY_PATH="/home/work/spider-home/"


mkdir -p $LOG_DIR $DEPLOY_PATH

function log_debug() {
    echo `date +"DEBUG: [%Y-%m-%d %k:%M:%S "` "$1" >> $LOG_FILE
    [[ $2 == "echo" ]] && echo $1
}

## 加载tag
source /home/work/module.conf

log_debug "hostTag is [$hostTag]" "echo"

sourceWebsiteList=`grep $hostTag task.conf | awk '{print $2}'`

log_debug "start to run task [$sourceWebsiteList]" "echo"

cd $DEPLOY_PATH && rm -rf spider-python
git clone git@git.bonbon.club:bbt/spider-python.git

## 杀掉还存在的进程
ps -eLf | grep run.sh | grep -v color | awk '{print $2}' | xargs -i kill -9 {}

for sourceWebsite in $sourceWebsiteList ; do
	log_debug "start to process [$sourceWebsite]" "echo"
	if [ $sourceWebsite"x" != "x" ];then
		cd $DEPLOY_PATH && mkdir -p $sourceWebsite && rsync -HavP spider-python/* $sourceWebsite/ 2>&1 >> $LOG_FILE
		cmd="cd $DEPLOY_PATH/$sourceWebsite && bash run.sh $sourceWebsite"
		#cmd="cd $DEPLOY_PATH/$sourceWebsite && echo 'aaaa'"
		eval $cmd >> $LOG_FILE 2>&1 &
		log_debug "run cmd is [$cmd]" "echo"
	fi
done

log_debug "finish task!"









