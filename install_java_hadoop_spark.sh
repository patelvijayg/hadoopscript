#!/bin/bash
#param 1 = default value (node)
mount_path=/home/vagrant/extras
rpm=$mount_path/rpm
sshfile=$mount_path/ssh
hadoopfiles=$mount_path/hadoopfiles
homepath=/home/vagrant

install_dir=/usr
export hadoop_binary=hadoop-2.7.6.tar.gz
export hadoop_version=hadoop-2.7.6
export spark_binary=spark-2.3.1-bin-hadoop2.7.tgz
export spark_version=spark-2.3.1-bin-hadoop2.7

echo "Installing JAVA"
sudo yum localinstall -y $rpm/jdk-8u181-linux-x64.rpm

echo "Installing HADOOP $spark_version"

sudo cp $rpm/$hadoop_binary $install_dir 

cd $install_dir 
sudo tar -xzf $hadoop_binary 
sudo rm -rf $hadoop_binary 
echo "ln -s $install_dir/$hadoop_version $install_dir/hadoop "
sudo ln -s $install_dir/$hadoop_version $install_dir/hadoop 

sudo mkdir -p $install_dir/hadoop/infra/namenode
sudo mkdir -p $install_dir/hadoop/infra/datanode

echo "Installing SPARK $hadoop_version"

sudo cp $rpm/$spark_binary $install_dir 
cd $install_dir 
sudo tar -xzf $spark_binary 
sudo rm -rf $spark_binary 
sudo ln -s $install_dir/$spark_version $install_dir/spark
mkdir -p $homepath/scripts/
cp -Rf $mount_path/scripts/* $homepath/scripts/
yum install epel-release -y
sudo yum -y install vim nano p7zip unzip net-tools tcpdump wget git
echo "Installation is successfully"
echo "Please run the $homepath/scripts/setup_variable.sh"