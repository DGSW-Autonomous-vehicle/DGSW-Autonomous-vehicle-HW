#!/bin/sh

curl http://www.linux-projects.org/listing/uv4l_repo/lrkey.asc | sudo apt-key add -

echo "deb http://www.linux-projects.org/listing/uv4l_repo/raspbian/ jessie main" >> /etc/apt/sources.list

sudo apt-get update
sudo apt-get install uv4l uv4l-raspicam

wget http://security.debian.org/debian-security/pool/updates/main/o/openssl/libssl1.0.0_1.0.1t-1+deb7u4_armhf.deb
sudo dpkg -i libssl1.0.0_1.0.1t-1+deb7u4_armhf.deb

sudo apt-get install uv4l-raspicam-extras

sudo apt-get install uv4l-server uv4l-uvc uv4l-xscreen uv4l-mjpegstream uv4l-dummy uv4l-raspidisp

sudo service uv4l_raspicam restart
