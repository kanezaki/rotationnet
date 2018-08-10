#!/bin/bash

##########
# case 2 #
##########

# compute and save scores.
for c in `cat classes_10.txt`
do
    python save_scores.py --center_only --gpu --mean_file VGG_mean.npy --images_dim 224,224 --model_def deploy_vggm_modelnet10_case2.prototxt --pretrained_model rotationnet_modelnet10_case2_ori2.caffemodel --input_file ModelNet10v2/test_full_$c.txt --output_file ModelNet10v2/test_full_$c.npy
done

# do prediction.
ncorrect=0
nsamp=0
for c in `cat classes_10.txt`
do
    res=`python classify_npyfile_case2_all_views.py ModelNet10v2/test_full_$c.npy $c classes_10.txt`
    echo $res
    tmp1=${res%%/*}
    tmp2=${res#*/}
    ncorrect=`expr $ncorrect + ${tmp1##*\(}`
    nsamp=`expr $nsamp + ${tmp2%)}`
done

echo "Total Accuracy:" `expr "scale=5; $ncorrect / $nsamp" | bc` 
