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
   Change 'caffe\_root' in save_scores.py to your path to caffe-rotationnet repository.  
   Run the demo script.  
  `$ bash demo.sh`

## Reproduce results on ModelNet40

### 1. Download multi-view images generated in [Su et al. 2015]
   `$ bash get_modelnet_png.sh`  
   [Su et al. 2015] H. Su, S. Maji, E. Kalogerakis, E. Learned-Miller. Multi-view Convolutional Neural Networks for 3D Shape Recognition. ICCV2015.  
   
### 2. Save scores and do predictions
   `$ bash test_modelnet40.sh`  

## Train your own RotationNet models
   Coming soon.