#!/bin/bash

echo '***************************************************************'
echo '                    Installing Packages                        '
echo '***************************************************************'
sudo apt-get install build-essential cmake -y
sudo apt-get install qt5-default libvtk6-dev -y
echo '*****************************************************'
sudo apt-get install libjpeg8-dev libtiff5-dev libjasper-dev libpng12-dev zlib1g-dev libwebp-dev libopenexr-dev libgdal-dev -y
echo '*****************************************************'
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev -y
sudo apt-get install libxvidcore-dev libx264-dev -y
echo '*****************************************************'
sudo apt-get install libgtk-3-dev -y
sudo apt-get install libatlas-base-dev gfortran -y
echo '*****************************************************'
sudo apt-get install python2.7-dev python3.5-dev -y
sudo apt-get install libdc1394-22-dev libtheora-dev libvorbis-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libxine2-dev -y
echo '***************************************************************'
echo '            Installing Numpy and Matplotlib                    '
echo '***************************************************************'
sudo apt-get install python3-numpy -y
sudo apt-get install python3-matplotlib -y
cd ~
echo '***************************************************************'
echo '                     Downloading OpenCV                        '
echo '***************************************************************'
wget -O opencv.zip https://github.com/Itseez/opencv/archive/3.1.0.zip
wget -O opencv_contrib.zip https://github.com/Itseez/opencv_contrib/archive/3.1.0.zip
unzip opencv_contrib.zip
unzip opencv.zip
cd ~/opencv-3.1.0/
mkdir build
cd build
echo '***************************************************************'
echo '                         Building Opencv                       '
echo '***************************************************************'
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_QT=ON -D WITH_OPENGL=ON -D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib-3.1.0/modules ..
make -j4
echo '***************************************************************'
echo '                       Installing Opencv                       '
echo '***************************************************************'
sudo make install
sudo ldconfig
echo '***************************************************************'
echo 'your cv version is (should be 3.1.0):'
python3 -c 'import cv2; print("Installed OpenCV Version: "); print(cv2.__version__)'
echo 'The installer script has completed.'
