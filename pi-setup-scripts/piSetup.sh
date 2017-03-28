#!/bin/bash

cd ~
echo "****************   UPDATING   ********************"
sudo apt-get update -y

echo "****************   INSTALLING PIP   ********************"
wget https://bootstrap.pypa.io/get-pip.py
sudo python get-pip.py
sudo python3 get-pip.py

echo "****************   INSTALING PYTHON PACKAGES   ********************"
sudo pip install numpy
sudo pip3 install numpy

sudo apt-get install i2c-tools python-smbus python-opengl python-pygame python-webpy -y

echo "****************   INSTALLING VNC SERVER ********************"
sudo apt-get install tightvncserver
cd /home/$USER/.config
mkdir autostart
cd autostart
echo "[Desktop Entry] Type=Application Name=TightVNC Exec=vncserver :1 StartupNotify=false" > tightvnc.desktop


echo "****************   CHANGING DESKTOP BACKGROUND  ********************"
pcmanfm --set-wallpaper ~/csrbot/pi-setup-scripts/robotBackground.png

echo "the installer script has completed."
