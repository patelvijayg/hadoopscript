#!/bin/bash
onefile=uPM_all_metrics-20180730080000-20180730081500.csv
cp $SCRIPT_DIR/datafiles/dataset1.7z /tmp/
cd /tmp
7za x dataset1.7z -y
hdfs dfs -mkdir /data1
hdfs dfs -put /tmp/dataset1/$onefile /data1
hdfs dfs -cat /data1/$onefile