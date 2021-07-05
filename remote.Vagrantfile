require "vagrant-aws"

class Hash
  def slice(*keep_keys)
    h = {}
    keep_keys.each { |key| h[key] = fetch(key) if has_key?(key) }
    h
  end unless Hash.method_defined?(:slice)
  def except(*less_keys)
    slice(*keys - less_keys)
  end unless Hash.method_defined?(:except)
end

Vagrant.configure("2") do |config|
  
  config.vm.box = "dummy"

  config.vm.network "forwarded_port", guest: 9000, host: 9000, host_ip: "127.0.0.1"

  config.vm.synced_folder "../lmsapi", "/home/vagrant/lmsapi", type: "rsync", owner: "lms-admin ", group:"lms-admin ", mount_options:["dmode=775,fmode=777"]
  
  config.vm.provision "shell", inline: "sudo service mysql start", run: "always"
  
  config.vm.provider :aws do |aws, override|
    aws.access_key_id = "AKIA2OHQWDGM5PTIVCF7"
    aws.secret_access_key = "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"
    aws.keypair_name = "lmspubkey"
    
    aws.ami = "ami-09e67e426f25ce0d7"
    aws.region = "us-east-1"
    aws.instance_type = "t2.micro"
    aws.security_groups = [ 'launch-wizard-1' ]
    
    override.ssh.username = "ubuntu"
    override.ssh.private_key_path = ".ssh/lmspubkey.pem"
  end
  
  config.vm.provider "virtualbox" do |v|
    v.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    v.customize ["modifyvm", :id, "--natdnsproxy1", "on"]
  end
  


end