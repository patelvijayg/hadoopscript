#!/bin/bash
onefile=companylist_noheader.csv
dir1=unittest
cp $SCRIPT_DIR/datafiles/data-master.7z /tmp/
cd /tmp
7za x data-master.7z -o./data-master -y
hdfs dfs -rm /$dir1
hdfs dfs -mkdir /$dir1
hdfs dfs -put /tmp/data-master/$onefile /$dir1
hdfs dfs -tail /$dir1/$onefile
