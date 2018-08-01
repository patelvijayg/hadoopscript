#!/bin/bash
onefile=uPM_all_metrics-20180730080000-20180730081500.csv
dir1=unittest
cp $SCRIPT_DIR/datafiles/dataset1.7z /tmp/
cd /tmp
7za x dataset1.7z -y
hdfs dfs -rm /$dir1
hdfs dfs -mkdir /$dir1
hdfs dfs -put /tmp/dataset1/$onefile /$dir1
hdfs dfs -cat /$dir1/$onefile