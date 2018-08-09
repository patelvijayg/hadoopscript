#!/bin/bash
.stophdall
.copyandsync
$SCRIPT_DIR/cleanall.sh
hdfs namenode -format
echo "DFS is reset"