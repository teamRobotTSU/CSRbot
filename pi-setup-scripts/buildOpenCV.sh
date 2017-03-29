#!/bin/bash

cd ~
sudo apt-get update -y
sudo apt-get install build-essential cmake pkg-config -y

wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
unzip opencv.zip
unzip opencv_contrib.zip
cd ~/opencv-3.1.0/
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D INSTALL_C_EXAMPLES=OFF \
-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules \
-D BUILD_EXAMPLES=ON ..
make
sudo make install
sudo ldconfig
echo "your cv version is (should be 3.1.0):"
python3 /home/$USER/csrbot/robot-scripts/cvVersion.py
echo "the installer script has completed."
