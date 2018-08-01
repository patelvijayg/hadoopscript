#!/bin/bash
echo "deleting $HADOOP_HOME/infra/namenode"
if [ -d $HADOOP_HOME/infra/namenode/ ]
then
	rm -rf $HADOOP_HOME/infra/namenode/*.*
fi

echo "deleting $HADOOP_HOME/infra/datanode"
if [ -d $HADOOP_HOME/infra/datanode/ ] 
then
	rm -rf $HADOOP_HOME/infra/datanode/*.*
fi

echo "deleting $HADOOP_HOME/logs"
if [ -d $HADOOP_HOME/logs ]
	rm -rf $HADOOP_HOME/logs/*.*
else
	mkdir -p $HADOOP_HOME/logs
fi

echo "deleting $SPARK_HOME/logs"
if [ -d $SPARK_HOME/logs ]
	rm -rf $SPARK_HOME/logs/*.*
else
	mkdir -p $SPARK_HOME/logs
fi

echo "deleted $HADOOP_HOME/hadoop/infra and $HADOOP_PREFIX/logs"

