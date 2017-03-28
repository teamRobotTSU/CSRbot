#!/bin/bash

cd ~
sudo apt-get update -y
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo python3 get-pip.py
sudo pip install numpy
sudo pip3 install numpy
sudo apt-get install i2c-tools -y

echo "the installer script has completed."
