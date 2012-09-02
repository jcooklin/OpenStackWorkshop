#!/bin/bash

#create user
for i in `shuf -i 2000-65000 -n 1`
do
echo ""
echo "creating user$i..."
adduser --disabled-password --gecos "" user${i}
echo "setting standard passwd for user$i..."
echo "user${i}:password" | chpasswd
echo "setup home dir..."
echo ". /opt/stack/devstack/openrc" >> /home/user${i}/.bashrc
echo "register account as available..."
echo ""
done
