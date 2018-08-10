#!/bin/bash

# download tar files
# modelnet10v2png_ori2.tar: 1.1 GB
# modelnet40v2png_ori4.tar: 2.7 GB
wget https://data.airc.aist.go.jp/kanezaki.asako/data/modelnet10v2png_ori2.tar
wget https://data.airc.aist.go.jp/kanezaki.asako/data/modelnet40v2png_ori4.tar

# extract tar files
mkdir -p ModelNet10v2
cd ModelNet10v2
tar xvf ../modelnet10v2png_ori2.tar
cd ..
cd ModelNet40v2
tar xvf ../modelnet40v2png_ori4.tar
cd ..
