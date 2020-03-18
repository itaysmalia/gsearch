#!/bin/sh
echo "installing..."
if [ $(id -u) -ne 0 ]; then
   echo "This script must be run as root" 
   exit 1
fi
mkdir ~/.gsearch
chown $SUDO_USER ~/.gsearch
chgrp $SUDO_USER ~/.gsearch
cp -v by.txt ~/.gsearch/by.txt
cp -v icon.txt ~/.gsearch/icon.txt
chown $SUDO_USER ~/.gsearch/*
chgrp $SUDO_USER ~/.gsearch/*
ln -s $( pwd )/gsearch.py /usr/bin/gsearch
echo "gsearch installed succesfuly"