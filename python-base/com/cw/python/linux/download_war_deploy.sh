#!/usr/bin/env bash
# 下载war包并发布shell脚本

tomcat_home=/home/apache-tomcat-8.5.15
SHUTDOWN=$tomcat_home/bin/shutdown.sh
STARTTOMCAT=$tomcat_home/bin/startup.sh

war_name=root.war
war_url=http://www.baidu.com/test.war
download_home=/home/download
bakup_home=/home/bak/tomcat-8.5.15/webapps

#1)下载war包到本地
#wget -P $download_home $war_url
wget $war_url -O $download_home/$war_name

#2)备份webapps目录
cp -r $tomcat_home/webapps/* $bakup_home/

#3)关闭$tomcat_home
echo "关闭$tomcat_home"
$SHUTDOWN
ps -ef |grep tomcat |grep $tomcat_home |grep -v 'grep'|awk '{print $2}' | xargs kill -9

#4)删除相关文件
#删除日志文件，如果你不先删除可以不要下面一行
#rm $tomcat_home/logs/* -rf
#删除tomcat的临时目录
rm $tomcat_home/work/* -rf

#5)将war包拷贝到webapps目录下
cp $download_home/$war_name $tomcat_home/webapps/

#6)启动tomcat
sleep 5
echo "启动$tomcat_home"
$STARTTOMCAT

#看启动日志
tail -f $tomcat_home/logs/catalina.out


