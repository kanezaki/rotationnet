#!/bin/bash

if [ $# -lt 1 ]
then
    echo "usage: bash make_reference_poses.sh [case1 or case2]"
    exit
fi

# case 1
if [ $1 = "case1" ]
then
    for c in `cat classes.txt`
    do
	# compute and save scores.
	python save_scores.py --center_only --gpu --model_def deploy_modelnet40_case1.prototxt --pretrained_model rotationnet_modelnet40_case1.caffemodel --input_file ModelNet40v1/train_$c.txt --output_file ModelNet40v1/train_$c.npy
	
	# do prediction.
	python classify_pose_estimate_npyfile_case1_all_views.py ModelNet40v1/train_$c.npy >ModelNet40v1/train_${c}_log.txt
	
	# make pose references.
	python make_reference_poses.py ModelNet40v1/train_$c.txt ModelNet40v1/train_${c}_log.txt >ModelNet40v1/reference_poses_${c}.txt
    done
fi

# case 2
if [ $1 = "case2" ]
then
    for c in `cat classes.txt`
    do
	# compute and save scores.
	python save_scores.py --center_only --gpu --model_def deploy_modelnet40_case2.prototxt --pretrained_model rotationnet_modelnet40_case2.caffemodel --input_file ModelNet40v2/train_$c.txt --output_file ModelNet40v2/train_$c.npy
	
	# do prediction.
	python classify_pose_estimate_npyfile_case2_all_views.py ModelNet40v2/train_$c.npy >ModelNet40v2/train_${c}_log.txt
	
	# make pose references.
	python make_reference_poses.py ModelNet40v2/train_$c.txt ModelNet40v2/train_${c}_log.txt >ModelNet40v2/reference_poses_${c}.txt
    done
fi

