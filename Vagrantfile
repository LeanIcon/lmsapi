Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"

  config.vm.network "forwarded_port", guest: 9000, host: 9000, host_ip: "127.0.0.1"

  config.vm.synced_folder "../lmsapi", "/home/vagrant/lmsapi", owner: "lms-admin ", group:"lms-admin ", mount_options:["dmode=755,fmode=664"]
  
  config.vm.provision "shell", inline: "sudo service mysql start", run: "always"

  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end

end