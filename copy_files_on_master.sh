#!/bin/bash
#it has to run only once after install_java_hadoop_spark file
homepath=/home/vagrant
hadoopfilesdir=$SCRIPT_DIR/hadoopfiles
sparkfilesdir=$SCRIPT_DIR/sparkfiles
echo "copying hadoop files from  $hadoopfiles to master node $HADOOP_HOME/etc/hadoop/"

cp -Rf $hadoopfilesdir/* $HADOOP_HOME/etc/hadoop/
#cp -Rf $hadoopfilesdir/*.xml $HADOOP_HOME/etc/hadoop/
#cp -Rf $hadoopfilesdir/*.sh $HADOOP_HOME/etc/hadoop/

cp -Rf $sparkfilesdir/* $SPARK_HOME/conf/

echo "Setup is successfully"
