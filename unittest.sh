#!/bin/bash
cd
7za x todetele.7z -y
hdfs dfs -mkdir /data1
hdfs dfs -put /home/vagrant/todetele/uPM_all_metrics-20180730080000-20180730081500.csv /data1
hdfs dfs -cat /data1/uPM_all_metrics-20180730080000-20180730081500.csv
