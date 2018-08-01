#!/bin/bash
#This script must be run from master node only
echo "cleanaing master node"
$SCRIPT_DIR/cleanfs.sh

echo "cleanaing slave nodes"

for slave in $(cat $HADOOP_CONF_DIR/slaves); do 
   echo "cleaning with $slave"
   ssh -t $slave "$SCRIPT_DIR/cleanfs.sh"
done

echo "Entire DFS is cleared"


