#!/bin/bash
#param 1 = hostname
hstname=$1
hstip=$2
echo "host-setttting parameters $1 , $2 "
mount_path=/home/vagrant/extras
homepath=/home/vagrant
sshfolder=$mount_path/sshfolder

if [[ ! -z "$hstname" ]]
then
	echo "changing host name to $hstname"
	sudo hostnamectl set-hostname $hstname --static
fi

sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
sudo echo "Host *" > $homepath/.ssh/config
sudo echo "StrictHostKeyChecking no" >> $homepath/.ssh/config

sudo chmod 0600 $homepath/.ssh/config
sudo systemctl restart sshd

#sudo chown -R vagrant:vagrant /home/vagrant/
cp -Rf $sshfolder/id_rsa* $homepath/.ssh/
cp -Rf $sshfolder/authorized_keys $homepath/.ssh/
chmod 600 $homepath/.ssh/authorized_keys
chmod 600 $homepath/.ssh/id_rsa*
sudo chown -R vagrant:vagrant $homepath/
IP_LIST=$(cat <<EOF
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
#hadoop dns entries
192.168.2.11  master1  m1
192.168.2.12  master2  m2
192.168.2.21  slave1  s1
192.168.2.22  slave2  s2
192.168.2.23  slave3  s3
192.168.2.24  slave4  s4
192.168.2.25  slave5  s5
192.168.2.26  slave6  s6
EOF
)
sudo echo "${IP_LIST}" > /etc/hosts
#ssh-keygen -t rsa -P '' -f $homepath/.ssh/id_rsa
#cat ~/.ssh/id_rsa.pub >> $homepath/.ssh/authorized_keys
echo "completed hostname changes"




vagrant box list
vagrant box remove mycentos7jdk
vagrant box add centos7hadoop package.box
vagrant up --provider virtualbox --debug
vagrant destroy -f

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	#slave
	(2..4).each do |i|
		config.vm.box = "centos7hadoop"
		config.vm.define :"node-s-#{i}" do |srvnode|
			srvnode.vm.network :private_network, ip: "192.168.2.2#{i}"
			srvnode.vm.provider "virtualbox" do |v|
				v.customize ["modifyvm", :id, "--memory", 768]
			end #Provider
	end #Config
  end #Loop Master
  
end #Main