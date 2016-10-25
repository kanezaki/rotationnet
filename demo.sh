#!/bin/bash

echo "Please input any key to start case 1."
read;

# compute and save scores.
python save_scores.py --center_only --gpu --model_def deploy_modelnet40_case1.prototxt --pretrained_model rotationnet_modelnet40_case1.caffemodel --input_file sample_case1_toilet_000000020.txt --output_file scores_case1_toilet_000000020.npy

# do prediction.
python classify_npyfile_case1.py sample_case1_toilet_000000020.txt scores_case1_toilet_000000020.npy


echo ""
echo "Please input any key to start case 2."
read;

# compute and save scores.
python save_scores.py --center_only --gpu --model_def deploy_modelnet40_case2.prototxt --pretrained_model rotationnet_modelnet40_case2.caffemodel --input_file sample_case2_toilet_000000020.txt --output_file scores_case2_toilet_000000020.npy

# do prediction.
python classify_npyfile_case2.py sample_case2_toilet_000000020.txt scores_case2_toilet_000000020.npy
