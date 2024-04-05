# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|

  config.vm.box = "debian/bullseye64"

  # Rabbit MQ management
  config.vm.network "forwarded_port", guest: 15672, host: 15672, auto_correct: true

  # HTTP for viewing coverage reports
  config.vm.network "forwarded_port", guest: 80, host: 8765

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update

    # Python
    apt-get install -y htop curl python3-pip build-essential python3 python3-setuptools
    sudo pip3 install --upgrade pip setuptools

    # Install deps
    sudo pip3 install -r /vagrant/requirements.txt
    sudo pip3 install nose2[coverage_plugin] coverage mock yapf nose2

    # .bashrc for default user
    echo """# .bashrc
    cd /vagrant""" > /home/vagrant/.bashrc

  SHELL

end
