#!/bin/bash
stophdall
$SCRIPT_DIR/cleanall.sh
$SCRIPT_DIR/copy_files_on_master.sh
$SCRIPT_DIR/syncnode.sh
hdfs namenode -format
echo "DFS is reset"