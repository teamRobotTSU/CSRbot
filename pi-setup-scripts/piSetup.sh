#!/bin/bash

cd ~
echo "****************   UPDATING   ********************"
sudo apt-get update -y

echo "****************   INSTALLING PIP   ********************"
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo python3 get-pip.py

echo "****************   INSTALING NUMPY   ********************"
sudo pip install numpy
sudo pip3 install numpy

echo "****************   INSTALLING I2C-TOOLS   ********************"
sudo apt-get install i2c-tools -y

echo "****************   CHANGING DESKTOP BACKGROUND  ********************"
pcmanfm --set-wallpaper ~/csrbot/pi-setup-scripts/robotBackground.png

echo "the installer script has completed."
