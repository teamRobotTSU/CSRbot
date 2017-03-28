#!/bin/bash

cd ~
echo "**************************************************"
echo "****************   UPDATING   ********************"
echo "**************************************************"
sudo apt-get update -y

echo "********************************************************"
echo "****************   INSTALLING PIP   ********************"
echo "********************************************************"
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo python3 get-pip.py

echo "********************************************************************"
echo "****************   INSTALING PYTHON3 PACKAGES   ********************"
echo "********************************************************************"
sudo pip install numpy
sudo pip3 install numpy
sudo pip3 install imutils
sudo pip3 install scipy

echo "********************************************************************"
echo "****************   INSTALLING PYTHON2 PACKAGES  ********************"
echo "********************************************************************"
sudo apt-get install i2c-tools python-smbus python-opengl python-pygame python-webpy -y

echo "*************************************************************"
echo "****************   INSTALLING VNC SERVER ********************"
echo "*************************************************************"
sudo apt-get install tightvncserver -y
printf "vncserver :1" >> .bashrc

echo "********************************************************************"
echo "****************   CHANGING DESKTOP BACKGROUND  ********************"
echo "********************************************************************"
pcmanfm --set-wallpaper ~/csrbot/pi-setup-scripts/robotBackground.png

echo "the installer script has completed."
