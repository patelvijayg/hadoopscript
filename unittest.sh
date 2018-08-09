#!/bin/bash
param=$1
loadful=${param:-"1"}
if [[ $loadful = "1" ]]
then
onefile=companylist_noheader.csv
dir1=unittest
7za x $SCRIPT_DIR/datafiles/data-master.7z -o/tmp/data-master -y
hdfs dfs -rm -r -f /$dir1
hdfs dfs -mkdir /$dir1
hdfs dfs -put /tmp/data-master/$onefile /$dir1
hdfs dfs -tail /$dir1/$onefile
echo "single file loaded for unit testing"
else
#data load
dir2=public
[[ ! -d /$dir2 ]] && mkdir /$dir2
sudo chown -R vagrant:vagrant /public
7za x $SCRIPT_DIR/datafiles/data-master.7z -o/$dir2 -y
hdfs dfs -rm -r -f /$dir2
hdfs dfs -mkdir /$dir2
hdfs dfs -put /tmp/data-master/* /$dir2/
hdfs dfs -tail /$dir2/companylist_noheader.csv
echo "schema public data is loaded"
fi

