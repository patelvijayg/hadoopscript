#!/bin/bash
#you can add the folder wish to delete during reset filesystem
listofdir=($HADOOP_HOME/infra/namenode $HADOOP_HOME/infra/datanode $HADOOP_HOME/logs $SPARK_HOME/logs /tmp/sparkevent)
for i in "${listofdir[@]}"
do
[[ -d $i ]] && rm -rf $i
echo "$i deleted ........" 
mkdir -p $i
echo "$i created ........" 
done

listofdir=($(echo /tmp/spark*))
for i in "${listofdir[@]}"
do
[[ -d $i ]] && rm -rf $i
	echo "$i deleted ........" 
done

echo "Completed the operation"
