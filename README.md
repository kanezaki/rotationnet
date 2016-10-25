# RotationNet

RotationNet classifies a partial set of multi-view images of an object.

## Install

### 1. Install caffe-rotationnet
  `$ git clone https://github.com/kanezaki/caffe-rotationnet.git`  
  `$ cd caffe-rotationnet`  
Prepare your Makefile.config and compile.  
  `$ make; make pycaffe`

### 2. Download scripts
  `$ git clone https://github.com/kanezaki/rotationnet.git`  
  `$ cd rotationnet`

### 3. Download pre-trained models
  `$ wget https://staff.aist.go.jp/kanezaki.asako/pretrained_models/rotationnet_modelnet40_case1.caffemodel`  
  `$ wget https://staff.aist.go.jp/kanezaki.asako/pretrained_models/rotationnet_modelnet40_case2.caffemodel`

## Getting started
   Change 'caffe_root' in save_scores.py to your path to caffe-rotationnet repository.  
   Run the demo script.  
  `$ bash demo.sh`
