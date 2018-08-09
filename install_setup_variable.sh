#!/bin/bash
homepath=/home/vagrant
scriptpath=/home/vagrant/scripts
export SPARK_HOME=/usr/spark
export HADOOP_HOME=/usr/hadoop

grep -q 'hadoop_variables.txt' $homepath/.bashrc
if [ $? -ne 0 ] 
then
	echo "adding the alias file into bashrc" 
	echo "source $scriptpath/alias.txt" >> $homepath/.bashrc
	echo "source $scriptpath/hadoop_variables.txt" >> $homepath/.bashrc
fi

if [ ! -f "$HOME/.pythonrc" ] 
then
echo 'import rlcompleter, readline' >> "$HOME/.pythonrc"
echo 'readline.parse_and_bind("tab: complete")'>> "$HOME/.pythonrc"
fi

sudo chown -R vagrant:vagrant $homepath/
sudo chown -R vagrant:vagrant $HADOOP_HOME/
sudo chown -R vagrant:vagrant $SPARK_HOME/
echo "Setup is successfully"