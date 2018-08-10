#!/bin/bash
onefile=shippers.json
dir1=northwind
7za x $SCRIPT_DIR/datafiles/northwind.7z -o/tmp/northwind -y
hdfs dfs -rm -r -f /$dir1
hdfs dfs -mkdir /$dir1
hdfs dfs -put /tmp/northwind/* /$dir1/
hdfs dfs -tail /$dir1/json/shippers.json