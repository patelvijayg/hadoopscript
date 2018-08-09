#!/bin/bash
onefile=companylist_noheader.csv
dir1=unittest
dir2=data
cp $SCRIPT_DIR/datafiles/data-master.7z /tmp/
cd /tmp
7za x data-master.7z -o./data-master -y
hdfs dfs -rm -r -f /$dir1
hdfs dfs -rm -r -f /$dir2
hdfs dfs -mkdir /$dir1
hdfs dfs -mkdir /$dir2
hdfs dfs -put /tmp/data-master/$onefile /$dir1
hdfs dfs -put /tmp/data-master/* /data/
hdfs dfs -tail /$dir1/$onefile