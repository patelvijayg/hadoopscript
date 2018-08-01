#!/bin/bash
#Enter the number of slave node so it will clean one by one all the nodes
for slave in $(cat $HADOOP_CONF_DIR/slaves); do 
   echo "syncing hadoop and scripts files with $slave"
   rsync -avzhe ssh $HADOOP_CONF_DIR/*.* vagrant@$slave:$HADOOP_CONF_DIR/
   rsync -avzhe ssh $SCRIPT_DIR/*.* vagrant@$slave:$SCRIPT_DIR/
done
for slave in $(cat $SPARK_CONF_DIR/slaves); do 
   echo "syncing spark with $slave"
   rsync -avzhe ssh $SPARK_CONF_DIR/*.* vagrant@$slave:$SPARK_CONF_DIR/
done
echo "sync process completed."

