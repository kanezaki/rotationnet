#!/usr/bin/env python
"""
classify.py is an out-of-the-box image classifer callable from the command line.

By default it configures and runs the Caffe reference ImageNet model.
"""
import numpy as np
import os
import sys
import argparse
import glob
import time

caffe_root = './caffe-rotationnet2/'  # Change this to your path.
sys.path.insert(0, caffe_root + 'python')

import caffe


def main(argv):
    pycaffe_dir = caffe_root + 'python/'

    parser = argparse.ArgumentParser()
    # Required arguments: input and output files.
    parser.add_argument(
        "--input_file",
        help="Input image, directory, or npy."
    )
    parser.add_argument(
        "--output_file",
        help="Output npy filename."
    )
    # Optional arguments.
    parser.add_argument(
        "--model_def",
        default=os.path.join(pycaffe_dir,
                "../examples/imagenet/imagenet_deploy.prototxt"),
        help="Model definition file."
    )
    parser.add_argument(
        "--pretrained_model",
        default=os.path.join(pycaffe_dir,
                "../examples/imagenet/caffe_reference_imagenet_model"),
        help="Trained model weights file."
    )
    parser.add_argument(
        "--gpu",
        action='store_true',
        help="Switch for gpu computation."
    )
    parser.add_argument(
        "--center_only",
        action='store_true',
        help="Switch for prediction from center crop alone instead of " +
             "averaging predictions across crops (default)."
    )
    parser.add_argument(
        "--images_dim",
        default='256,256',
        help="Canonical 'height,width' dimensions of input images."
    )
    parser.add_argument(
        "--mean_file",
        default=os.path.join(pycaffe_dir,
                             'caffe/imagenet/ilsvrc_2012_mean.npy'),
        help="Data set image mean of H x W x K dimensions (numpy array). " +
             "Set to '' for no mean subtraction."
    )
    parser.add_argument(
        "--input_scale",
        type=float,
        default=255,
        help="Multiply input features by this scale before input to net"
    )
    parser.add_argument(
        "--channel_swap",
        default='2,1,0',
        help="Order to permute input channels. The default converts " +
             "RGB -> BGR since BGR is the Caffe default by way of OpenCV."

    )
    parser.add_argument(
        "--ext",
        default='jpg',
        help="Image file extension to take as input when a directory " +
             "is given as the input file."
    )
    args = parser.parse_args()

    image_dims = [int(s) for s in args.images_dim.split(',')]
    channel_swap = [int(s) for s in args.channel_swap.split(',')]

    mean = None
    if args.mean_file:
        mean = np.load(args.mean_file)
        # Resize mean (which requires H x W x K input in range [0,1]).
        in_shape = image_dims
        m_min, m_max = mean.min(), mean.max()
        normal_mean = (mean - m_min) / (m_max - m_min)
        mean = caffe.io.resize_image(normal_mean.transpose((1,2,0)),
                                     in_shape).transpose((2,0,1)) * (m_max - m_min) + m_min

    if args.gpu:
        caffe.set_mode_gpu()
        print("GPU mode")
    else:
        caffe.set_mode_cpu()
        print("CPU mode")

    # Make classifier.
    classifier = caffe.Classifier(args.model_def, args.pretrained_model,
            image_dims=image_dims, mean=mean,
            input_scale=1.0, raw_scale=255.0, channel_swap=channel_swap)

    # Load image file.
    args.input_file = os.path.expanduser(args.input_file)
    f = open(args.input_file)
    im_files_ = f.readlines()
    im_files = []
    for i in range(len(im_files_)):
        im_f = im_files_[ i ].split( ' ' )
        if len(im_f) == 1:
            im_f[ 0 ] = im_f[ 0 ][:-1]
        im_files.append(im_f[ 0 ])

    inputs =[caffe.io.load_image(im_f) for im_f in im_files]

    print "Classifying %d inputs." % len(inputs)

    # Classify.
    start = time.time()
    predictions = classifier.predict(inputs, not args.center_only)
    print "Done in %.2f s." % (time.time() - start)

    # Save
    np.save(args.output_file, predictions)
    print "Saved %s." % args.output_file


if __name__ == '__main__':
    main(sys.argv)
