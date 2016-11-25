# RotationNet

RotationNet classifies a partial set of multi-view images of an object.  

![RotationNet](https://staff.aist.go.jp/kanezaki.asako/images/RotationNet.jpg "Inference Process")

Asako Kanezaki, Yasuyuki Matsushita and Yoshifumi Nishida.
**RotationNet: Joint Learning of Object Classification and Viewpoint Estimation using Unaligned 3D Object Dataset.** 
*arXiv preprint arXiv:1603.06208*, 2016.
([pdf](https://arxiv.org/abs/1603.06208))


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

### 1. Download multi-view images generated in [Su et al. 2015] (the same as above)  
   `$ bash get_modelnet_png.sh`  

### 2. Download initial weights for fine-tuning the models
   Please download the file "ilsvrc_2012_train_iter_310k" according to [R-CNN repository](https://github.com/rbgirshick/rcnn)  
   This is done by the following command:  
    `$ wget http://www.cs.berkeley.edu/~rbg/r-cnn-release1-data.tgz`  
    `$ tar zxvf r-cnn-release1-data.tgz`  

### 3. Run the training operation
#### 3-1. Case (2): Train the model w/o upright orientation (RECOMMENDED)
    `$ GLOG_logtostderr=1 ./caffe-rotationnet/build/tools/finetune_net.bin Training/rotationnet_modelnet40_case2_solver.prototxt caffe_nets/ilsvrc_2012_train_iter_310k 2>&1 | tee log.txt`  
#### 3-2. Case (1): Train the model with upright orientation
    `$ GLOG_logtostderr=1 ./caffe-rotationnet/build/tools/finetune_net.bin Training/rotationnet_modelnet40_case1_solver.prototxt caffe_nets/ilsvrc_2012_train_iter_310k 2>&1 | tee log.txt`  
