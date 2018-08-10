#!/bin/bash

##########
# case 2 #
##########

# compute and save scores.
for c in `cat classes.txt`
do
    python save_scores.py --center_only --gpu --mean_file VGG_mean.npy --images_dim 224,224 --model_def deploy_vggm_modelnet40_case2.prototxt --pretrained_model rotationnet_modelnet40_case2_ori4.caffemodel --input_file ModelNet40v2/test_full_$c.txt --output_file ModelNet40v2/test_full_$c.npy
done

# do prediction.
ncorrect=0
nsamp=0
for c in `cat classes.txt`
do
    res=`python classify_npyfile_case2_all_views.py ModelNet40v2/test_full_$c.npy $c`
    echo $res
    tmp1=${res%%/*}
    tmp2=${res#*/}
    ncorrect=`expr $ncorrect + ${tmp1##*\(}`
    nsamp=`expr $nsamp + ${tmp2%)}`
done

echo "Total Accuracy:" `expr "scale=5; $ncorrect / $nsamp" | bc` 
