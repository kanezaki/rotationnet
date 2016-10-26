#!/bin/bash

##########
# case 1 #
##########

# compute and save scores.
for c in `cat classes.txt`
do
    python save_scores.py --center_only --gpu --model_def deploy_modelnet40_case1.prototxt --pretrained_model rotationnet_modelnet40_case1.caffemodel --input_file ModelNet40v1/test_$c.txt --output_file ModelNet40v1/test_$c.npy
done

# do prediction.
for c in `cat classes.txt`
do
    python classify_npyfile_case1_all_views.py ModelNet40v1/test_$c.npy $c
done

##########
# case 2 #
##########

# compute and save scores.
for c in `cat classes.txt`
do
    python save_scores.py --center_only --gpu --model_def deploy_modelnet40_case2.prototxt --pretrained_model rotationnet_modelnet40_case2.caffemodel --input_file ModelNet40v2/test_$c.txt --output_file ModelNet40v2/test_$c.npy
done

# do prediction.
for c in `cat classes.txt`
do
    python classify_npyfile_case2_all_views.py ModelNet40v2/test_$c.npy $c
done
