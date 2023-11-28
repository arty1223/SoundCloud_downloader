# ices0 installer
#!/bin/bash
sudo apt install icecast2
wget https://downloads.xiph.org/releases/ices/ices-0.4.tar.gz
tar -xvf ices-0.4.tar.gz 
cd ices-0.4/
sudo apt install lame make
sudo apt install libmp3lame-dev libxml2-dev libshout-dev libvorbis-dev
./configure --prefix=/usr/local --with-pic --with-lame
cd ices-0.4/
sudo make install
cd -
echo "Now you should setup ices.conf (located in cp /usr/local/etc/ices.conf.dist)"