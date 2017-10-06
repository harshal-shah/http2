#!/bin/bash

apt-get update -y
apt-get install -y build-essential nghttp2 libnghttp2-dev wget python3 python3-dev python3-pip build-essential libssl-dev libffi-dev
pip3 install pyOpenSSL
cd /tmp
wget https://curl.haxx.se/download/curl-7.54.0.tar.bz2
tar -xvjf curl-7.54.0.tar.bz2
cd curl-7.54.0
./configure --with-nghttp2 --prefix=/usr/local
make
make install
ldconfig
cd /app/
