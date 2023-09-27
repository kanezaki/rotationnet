# RotationNet

RotationNet takes multi-view images of an object as input and jointly estimates its pose and object category.  

![RotationNet](https://kanezaki.github.io/media/RotationNet2.jpg "Inference Process")

Asako Kanezaki, Yasuyuki Matsushita and Yoshifumi Nishida.
**RotationNet: Joint Object Categorization and Pose Estimation Using Multiviews from Unsupervised Viewpoints.** 
*CVPR*, pp.5010-5019, 2018.
([pdf](https://arxiv.org/abs/1603.06208))
([project](https://kanezaki.github.io/rotationnet/))

## News

[2018.08.10] We uploaded the scripts and pre-trained models that <span style="color:red">reproduce our BEST results on ModelNet10 and ModelNet40.</span>

[2017.02] We got **the first prize** at [the SHREC2017 RGB-D Object-to-CAD Retrieval Contest](http://people.sutd.edu.sg/~saikit/projects/sceneNN/shrec17/evaluation/)!  
[2017.02] We got **the first prize** at Task 1 in [the SHREC2017 Large-scale 3D Shape Retrieval from ShapeNet Core55 Challenge](https://shapenet.cs.stanford.edu/shrec17/#results)!  
Please see [SHREC2017\_track3 repository](https://github.com/kanezaki/SHREC2017_track3) to reproduce our results on SHREC2017 track3.  


## Requirement

### 1. Prepare [caffe-rotationnet2](https://github.com/kanezaki/caffe-rotationnet2)
    $ git clone https://github.com/kanezaki/caffe-rotationnet2.git  
    $ cd caffe-rotationnet2  
  
Prepare your Makefile.config and compile.  

    $ make; make pycaffe

### 2. Download scripts
    $ git clone https://github.com/kanezaki/rotationnet.git  
    $ cd rotationnet

### 3. Download pre-trained models
Models trained on ModelNet10 and ModelNet40 (full set)  

    $ wget https://data.airc.aist.go.jp/kanezaki.asako/pretrained_models/rotationnet_modelnet10_case2_ori2.caffemodel  
    $ wget https://data.airc.aist.go.jp/kanezaki.asako/pretrained_models/rotationnet_modelnet40_case2_ori4.caffemodel  

Models trained on ModelNet40 (subset)  

    $ wget https://data.airc.aist.go.jp/kanezaki.asako/pretrained_models/rotationnet_modelnet40_case1.caffemodel  
    $ wget https://data.airc.aist.go.jp/kanezaki.asako/pretrained_models/rotationnet_modelnet40_case2.caffemodel

## Getting started
   Change 'caffe\_root' in save_scores.py to your path to caffe-rotationnet2 repository.  
   Run the demo script.  

    $ bash demo.sh

   This predicts the category of testing images. Please see below and run "demo2.sh" for testing pose estimation.  


## Reproduce <span style="color:red">our best</span> results on ModelNet10 and ModelNet40 (full set)

### 1. Download multi-view images 
    $ bash get_full_modelnet_png.sh  
   
### 2. Save scores and do predictions
    $ bash test_full_modelnet10.sh  
    $ bash test_full_modelnet40.sh  

## Reproduce results on ModelNet40 (subset)

### 1. Download multi-view images generated in [Su et al. 2015]
    $ bash get_modelnet_png.sh  
[Su et al. 2015] H. Su, S. Maji, E. Kalogerakis, E. Learned-Miller. Multi-view Convolutional Neural Networks for 3D Shape Recognition. ICCV2015.  
   
### 2. Save scores and do predictions
    $ bash test_modelnet40.sh  

## Train your own RotationNet models

### 1. Download multi-view images generated in [Su et al. 2015]
    $ bash get_modelnet_png.sh  

### 2. Download initial weights for fine-tuning the models
   Please download the file "ilsvrc_2012_train_iter_310k" according to [R-CNN repository](https://github.com/rbgirshick/rcnn)  
   This is done by the following command:  

    $ wget http://www.cs.berkeley.edu/~rbg/r-cnn-release1-data.tgz  
    $ tar zxvf r-cnn-release1-data.tgz  

### 3. Run the training operation
#### 3-1. Case (2): Train the model w/o upright orientation (RECOMMENDED)
    $ ./caffe-rotationnet2/build/tools/caffe train -solver Training/rotationnet_modelnet40_case2_solver.prototxt -weights caffe_nets/ilsvrc_2012_train_iter_310k 2>&1 | tee log.txt  
#### 3-2. Case (1): Train the model with upright orientation
    $ ./caffe-rotationnet2/build/tools/caffe train -solver Training/rotationnet_modelnet40_case1_solver.prototxt -weights caffe_nets/ilsvrc_2012_train_iter_310k 2>&1 | tee log.txt  


## Test pose estimation

### 1. (If not done,) download multi-view images generated in [Su et al. 2015]
    $ bash get_modelnet_png.sh  
[Su et al. 2015] H. Su, S. Maji, E. Kalogerakis, E. Learned-Miller. Multi-view Convolutional Neural Networks for 3D Shape Recognition. ICCV2015.  
   
### 2. Align objects in the training set
    $ bash make_reference_poses.sh case1 # for case (1)  
    $ bash make_reference_poses.sh case2 # for case (2)   

   This predicts the viewpoints of training images and writes the image file paths in the predicted order.  


### 3. Run the demo script  
    $ bash demo2.sh

   This predicts the category and viewpoints of testing images, and then displays 10 training objects in the predicted category seen from the predicted viewpoints.  


## Reproduce results on SHREC2017 track3 (Large-scale 3D Shape Retrieval from ShapeNet Core55)
   Please see [SHREC2017\_track3 repository](https://github.com/kanezaki/SHREC2017_track3)


## License

BSD