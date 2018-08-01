#!/bin/bash
#param 1 = default value (node)
#export HADOOP_HOME=/usr/hadoop
$HADOOP_HOME/sbin/yarn-daemon.sh $1 nodemanager
$HADOOP_HOME/sbin/hadoop-daemon.sh $1 datanode
echo $(cat /etc/hostname)" is $1 successfully "