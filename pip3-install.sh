#!/usr/bin/env bash
# 本机Mac pip安装脚本 因之前修改过ssl，懒得改回去了

if [[ $$ -lt 1 ]]; then
	echo "You should give at least one param"
else
	pip3 install $1 -i http://pypi.douban.com/simple --trusted-host pypi.douban.com
fi
