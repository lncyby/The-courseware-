#! /bin/bash

cd 
rm  filedir -rf
rm  dirdir  -rf 

mkdir filedir
mkdir dirdir

if [ -f $1 ]
then
    cd filedir
    touch $1
if [ -f $2 ] 
then
    cd dirdir
    mkdir $2

fi
tar czf filedir.tar.gz filedir

tar cjf dirdir.tar.bz2 dirdir

sudo mv filedir.tar.gz /mnt/hgfs/share

sudo mv dirdir.tar.bz2 /mnt/hgfs/share

cd /mnt/hgfs/share

 
tar xvf filedir.tar.gz 

tar xvf dirdir.tar.bz2 




echo "king"
