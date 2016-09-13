#!/bin/bash

ANSIBLE_PULL=/usr/bin/ansible-pull

[ -x $ANSIBLE_PULL ] || sudo apt-get install -y ansible
[ -x /usr/bin/git ] || sudo apt-get install -y git

if [ -x $ANSIBLE_PULL ]
then
    echo "localhost ansible_connection=local" > /tmp/local_node_inventory
    $ANSIBLE_PULL --url=https://github.com/profitware/webdev-hosting.git -i /tmp/local_node_inventory
else
    echo "Cannot find or install Ansible. Exiting."
fi
