IPADDR = "192.168.30.101"
NETMASK = "255.255.255.0"
GATEWAY = "192.168.30.1"
VMNAME = "hosting"

Vagrant.configure("2") do |config|
  config.vm.define VMNAME do |d|
    config.vm.provider "virtualbox" do |v|
      v.memory = 2048
      v.cpus = 2
      v.name = VMNAME
      v.linked_clone = true
    end
  end

  config.vm.box = "ubuntu/trusty64"
  config.vm.network "private_network",
    adapter: 2,
    name: "vboxnet0",
    ip: IPADDR,
    netmask: NETMASK,
    gateway: GATEWAY,
    auto_config: false

  config.vm.provision :shell, inline: <<-SCRIPT
    sudo hostnamectl set-hostname #{VMNAME}
  SCRIPT

  config.vm.provision :shell do |shell|
    shell.inline = <<-SCRIPT
      sudo ifconfig eth1 #{IPADDR} netmask #{NETMASK} up
      sudo ip route replace default via #{GATEWAY} dev eth1
    SCRIPT
  end

  config.vm.provision :shell, inline: <<-SCRIPT
    sysctl -w net.ipv6.conf.all.disable_ipv6=1
    sysctl -w net.ipv6.conf.default.disable_ipv6=1
    sysctl -w net.ipv6.conf.lo.disable_ipv6=1
  SCRIPT


  config.vm.provision :shell, inline: <<-SCRIPT
    sudo sed -i 's|[#]*PasswordAuthentication yes|PasswordAuthentication no|g' /etc/ssh/sshd_config
    sudo sed -i 's|UsePAM yes|UsePAM no|g' /etc/ssh/sshd_config
    sudo sed -i 's|PermitRootLogin without-password|PermitRootLogin no|g' /etc/ssh/sshd_config
    sudo service ssh restart
  SCRIPT

  config.vm.provision :shell, inline: <<-SCRIPT
    sudo apt-get install -y git nginx shellinabox ipython python-ipdb

    sudo rm /etc/nginx/sites-enabled/default
    sudo rm /etc/default/shellinabox

    sudo ln -s /vagrant/conf/hosting.conf /etc/nginx/sites-enabled/hosting.conf
    sudo ln -s /vagrant/conf/shellinabox /etc/default/shellinabox
    sudo ln -s /vagrant/bin/newuser.sh /usr/local/bin/u
    sudo chmod a+x /usr/local/bin/u

    sudo mkdir /etc/skel/www
    ln -s /vagrant/www /home/vagrant/www

    sudo service nginx restart
    sudo service shellinabox restart
  SCRIPT
end
