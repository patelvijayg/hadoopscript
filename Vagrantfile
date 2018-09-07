VAGRANTFILE_API_VERSION = "2"
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

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

	nodes.each do |cust_node|
		config.vm.box = "centos7hadoop"
		config.vm.define :"#{cust_node[:hostname]}" do |srvnode|
			srvnode.vm.hostname = cust_node[:hostname]
			srvnode.vm.network :private_network, ip: cust_node[:ip]
			srvnode.vm.provider "virtualbox" do |v|
			  v.customize ["modifyvm", :id, "--memory", cust_node[:mem]]
			srvnode.vm.provision "shell", inline: $script
			end #Provider
		end #define	
	end #cust_node
 
end #Main

