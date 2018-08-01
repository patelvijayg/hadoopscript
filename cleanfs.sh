#!/bin/bash
echo "deleting $HADOOP_HOME/infra/namenode"

[ -d $HADOOP_HOME/infra/namenode ] && rm -rf $HADOOP_HOME/infra/namenode
[ -d $HADOOP_HOME/infra/datanode ] && rm -rf $HADOOP_HOME/infra/datanode
[ -d $HADOOP_HOME/logs ] && rm -rf $HADOOP_HOME/logs
[ -d $SPARK_HOME/logs ] && rm -rf $SPARK_HOME/logs
mkdir -p $HADOOP_HOME/infra/namenode
mkdir -p $HADOOP_HOME/infra/datanode
mkdir -p $HADOOP_HOME/logs
mkdir -p $SPARK_HOME/logs

echo "deleted $HADOOP_HOME/hadoop/infra and $HADOOP_PREFIX/logs"
