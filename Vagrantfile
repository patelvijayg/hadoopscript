VAGRANTFILE_API_VERSION = "2"
$sshsetup = <<-SSHSETTING
[[ ! -d /home/vagrant/.ssh/ ]] && mkdir -p /home/vagrant/.ssh
KEY_STR1='ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDCsL0Q33EL9Xe2jzd9l+Fft/cse5NCDI3uicDZGn4eu8hsik0yaKS91JR8u87npziT6Bu6dYqyrtm73Lo09MG8GM9a+RldGm0pU1nzEDNWtG2NYJJnKGxHNvYhYZsliQrX33IM51ChX+r/xhSJRwwdpb16s+OxKZ+5vwpPmy7U0KeKsLWGWW4f+zd+RnrDBFQp7GHlzg57KmQPv8E2UYUZFQskg97bswUJGqfLhDSyULTtZBP5nJJIB76oVR7R48GRMISy68NYiTuP5uuzbkGmweoPHQzFD9nb3/Ja0qWZoQc4/V6CkvOArGbx+q6uekrY8YQrK0vPGQ15Pl2uGEtd vagrant@master1' 
KEY_STR2='ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEAxS4eA1yQkk9kGtz8xrgvbSUrMVMYyFuFjv2uWBEQAVyfLyRjeicxZ4XU8fOhNBNzEEPozPXhh/atbAVyKuyryKJakNrt2zF7A0U9tzM9KpBxA/us7IsYt3sSjmxhJl+YrZHaph3siEN1SkzrKwTh9G/1l/H/G/JAgHCBhwPlG4M= rsa 1024-022818'
ID_RSA_STR=$(cat <<EOF
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAwrC9EN9xC/V3to83fZfhX7f3LHuTQgyN7onA2Rp+HrvIbIpN
MmikvdSUfLvO56c4k+gbunWKsq7Zu9y6NPTBvBjPWvkZXRptKVNZ8xAzVrRtjWCS
ZyhsRzb2IWGbJYkK199yDOdQoV/q/8YUiUcMHaW9erPjsSmfub8KT5su1NCnirC1
hlluH/s3fkZ6wwRUKexh5c4OeypkD7/BNlGFGRULJIPe27MFCRqny4Q0slC07WQT
+ZySSAe+qFUe0ePBkTCEsuvDWIk7j+brs25BpsHqDx0MxQ/Z29/yWtKlmaEHOP1e
gpLzgKxm8fqurnpK2PGEKytLzxkNeT5drhhLXQIDAQABAoIBAFNAMBie80Ah3ub5
psjVwVGk4NTsorODms19qjEr2vJZagK/wPLlPEzQMg6EYJ0+LDtS7Uh2KrDtg72J
TTaH0rAUC9bi3a2qNzOMqNH/A3T4AkCKIxBpgKOTJPxxOF58k15r9eD+qMPYuCxX
D0EEWHH1BWkKszp2ig5rWoVf3k6xi0wYMaZTzzFXF7/Sg8AoWp0fQ4z9I1nigQJ8
aWCWlcPFCXgvr5jAUBCvVxDXBQBD+eWGgX7tt/OFOiHkiGqWhBU9ZcAcy2AKqeDE
6RJhraLBS8H9sOEPweyUCoeFmv7CPWbRMCS/laXJQCI6OR9CezL8SWgG1Zi9Jm1P
lu9RUyECgYEA6k1UmUN+CsW/Ju1mzM/cxJGVBO9uQtVWGalwf6HAKMP5zPJ2wPH9
xWOkdJOCpwk86UYes289NHquWq2I2l+8XcW4xvIKmFB5dmCu1S4cKIG5+FYuCg5X
3xZJsJIc5AXre/p7Xla9jgsNGsiwoFtvV9MOvbsAKJfQSEOQWL2yFIcCgYEA1LhS
aU0chnT/Ze76+pYotHNYdARTg9GfuDGRuVAqQnDHOdYIXl2dMqECXsXfTGgG6eUX
22lrp3Sn07o1CxYCbGJKsk12cGncYJg/FjwkbET6EpQWhVHKAMxBffg1/SurDjG7
Thf1T3yAegYdvR5kYIUyPw3fmCXwbIp4jxIWPfsCgYAqw/afCtykprdfKZHL7FzF
XDUw82rStBHFGVI5WZKzXiHoMJFQYlsJfkh0JsCAMIV3pp7P7YvkWkgcsPP7t+Gv
0/kIBwG8D2Q8ISWIL6RgGF2TYFeC6l9LjsvgeKrhS9tRg8Sk0XxDwuyfaOYkPswx
4YodQ1aiEiOoLPzZ1bX9XQKBgQCggGcmLtmsFhEyr0vN0YjrBvEhsLX3Cy7xQu2K
HpOUSBX6bKUp1oaq0dPBAJoIw6Eb0BDdK8Dfu+R5m9E0CSpQ7yUfPdV04ls2wwku
1LhCvRTW+ce4VksNqRBtZOAPo2hQsHN8bBVbITyrVXwQ2yKvtTCBZQ1ldpLewuhO
Qz5nCwKBgADLMhe6xjpqS3eqjQBqMh44zv+hHcIpHzJLm0AoMjJBce2I4falDub3
OSD/aTofqRFVi3xjjNORO1xhANN1tDXA1VLRLyqkwSQdnCyutweGE1og3pbFl+SS
lJTM/TQkDG0hZz6108JLHBwv5VKCHPoitlEhpdj9h3T0MNE1XTHu
-----END RSA PRIVATE KEY-----
EOF
)
sudo echo "${ID_RSA_STR}" > /home/vagrant/.ssh/id_rsa
sudo echo "${KEY_STR1}" >> /home/vagrant/.ssh/authorized_keys
sudo echo "${KEY_STR1}" > /home/vagrant/.ssh/id_rsa.pub
sudo echo "${KEY_STR2}" >> /home/vagrant/.ssh/authorized_keys
sudo echo "${KEY_STR2}" > /home/vagrant/.ssh/Vijay_rsa1024.pub

sudo sed -i 's/PasswordAuthentication no/PasswordAuthentication yes/g' /etc/ssh/sshd_config
sudo echo "Host *" > /home/vagrant/.ssh/config
sudo echo "StrictHostKeyChecking no" >> /home/vagrant/.ssh/config

sudo hostnamectl set-hostname master --static
sudo systemctl restart sshd
SSHSETTING

$installation = <<-INSTALLATION
sudo yum install epel-release -y
sudo yum -y install vim nano p7zip unzip net-tools tcpdump wget nc git
echo "installing java............"
sudo yum install -y java-1.8.0-openjdk-devel

git clone https://github.com/patelvijayg/hadoopscript.git /home/vagrant/scripts
echo '[[  -f /home/vagrant/scripts/alias.txt ]] && source /home/vagrant/scripts/alias.txt' >> /home/vagrant/.bashrc
echo '[[  -f /home/vagrant/scripts/hadoop_variables.txt ]] && source /home/vagrant/scripts/hadoop_variables.txt' >> /home/vagrant/.bashrc

echo 'import rlcompleter, readline' >> "/home/vagrant/.pythonrc"
echo 'readline.parse_and_bind("tab: complete")'>> "/home/vagrant/.pythonrc"

echo "Java installtion completed"
INSTALLATION


$hadoopinstallation = <<-HINSTALLATION
export hadoop_binary=hadoop-2.7.6.tar.gz
export hadoop_version=hadoop-2.7.6
export spark_binary=spark-2.3.1-bin-hadoop2.7.tgz
export spark_version=spark-2.3.1-bin-hadoop2.7
rpm=/home/vagrant/rpm
install_dir=/usr

echo "Hadoop & spark Downloading started"

[[ ! -d ${rpm} ]] && mkdir -p  ${rpm}
cd ${rpm}
wget -c https://archive.apache.org/dist/hadoop/core/hadoop-2.7.6/hadoop-2.7.6.tar.gz 2>/dev/null
wget -c https://www.apache.org/dist/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz 2>/dev/null

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
sudo rm $rpm/$spark_binary 
sudo rm $rpm/$hadoop_binary 
echo "Hadoop installtion completed"

[[ ! -d /public ]] && mkdir /public
[[ ! -d /tmp/spark ]] && mkdir -p /tmp/spark
sudo chown -R vagrant:vagrant /home/vagrant/
sudo chown -R vagrant:vagrant $install_dir/$hadoop_version/
sudo chown -R vagrant:vagrant $install_dir/$spark_version/
sudo chown -R vagrant:vagrant /public/
sudo chown -R vagrant:vagrant /tmp/spark/
sudo chmod 400 /home/vagrant/.ssh/id_rsa
echo "192.168.56.201 	master1		slave1" >> /etc/hosts
echo "Installation done succesfully"
echo "now loagin as vagrant and run  .copyandsync and reset_factory.sh and .starthdfs and unittest.sh"
HINSTALLATION




Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
	(1..1).each do |i|
	#nodes.each do |cust_node|
		config.vm.box = "centos/7"
		config.vm.define :"master-#{i}" do |srvnode|
			srvnode.vm.network :private_network, ip: "192.168.56.201"
			#srvnode.vm.network :private_network, ip: "192.168.56.20#{i}"
			srvnode.vm.network "public_network"
			srvnode.ssh.insert_key = false
			srvnode.vm.provider "virtualbox" do |v|
				v.customize ["modifyvm", :id, "--memory", 1024]
			end #Provider
			srvnode.vm.provision "shell", inline: $sshsetup	
			srvnode.vm.provision "shell", inline: $installation	
			srvnode.vm.provision "shell", inline: $hadoopinstallation	
			#srvnode.vm.provision "shell", inline: $script
	end #define
  end #each Loop 
end #configure

########################This will be use for create the cluster
nodes = [
{:hostname=>"master1", :ip =>"192.168.2.11", :mem =>1024},
{:hostname=>"slave1", :ip =>"192.168.2.21", :mem =>768},
{:hostname=>"slave2", :ip =>"192.168.2.22", :mem =>768},
{:hostname=>"slave3", :ip =>"192.168.2.23", :mem =>768}
]

$script = <<-SCRIPT
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
SCRIPT

#Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
#	nodes.each do |cust_node|
#		config.vm.box = "centos7hadoop"
#		config.vm.define :"#{cust_node[:hostname]}" do |srvnode|
#			srvnode.vm.hostname = cust_node[:hostname]
#			srvnode.vm.network :private_network, ip: cust_node[:ip]
#			srvnode.vm.provider "virtualbox" do |v|
#				v.customize ["modifyvm", :id, "--memory", cust_node[:mem]]
#			srvnode.vm.provision "shell", inline: $script
#			end #Provider v
#		end #define	 srvnode
#	end #each cust_node
#end #configure

#vagrant box list
#vagrant box remove centos7hadoop
#vagrant package --output centos7hadoop.box
#vagrant box add centos7hadoop centos7hadoop.box
#vagrant up --provider virtualbox --debug
#vagrant destroy -f