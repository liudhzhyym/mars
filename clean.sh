#!/bin/bash

## 杀掉还存在的进程
ps -eLf | grep pic | grep -v color | awk '{print $2}' | xargs -i kill -9 {}

find . -name *.pyc | xargs -i rm {}









