#!/bin/bash
cd $SCRIPT_DIR
git reset --hard FETCH_HEAD 
git pull
chmod +wx -R *
echo "latst copy checked-out"
