"""
code copied from https://github.com/cbfinn/maml/blob/master/data/miniImagenet/proc_images.py
Script for converting from csv file datafiles to a directory for each image (which is how it is loaded by MAML code)

Acquire miniImagenet from Ravi & Larochelle '17, along with the train, val, and test csv files. Put the
csv files in the miniImagenet directory and put the images in the directory 'miniImagenet/images/'.
Then run this script from the miniImagenet directory:
    cd data/miniImagenet/
    python proc_images.py
"""

from __future__ import print_function
import csv
import glob
import os

from PIL import Image

all_classes = []
all_images = []
path_to_classes = '/home/zhuhaozhe/data/L1/'
L1 = glob.glob(path_to_classes + '*')
all_classes += glob.glob(path_to_classes + '*')
for c in os.listdir(path_to_classes):
    path_to_images = os.path.join(path_to_classes, c) + '/'
    all_images += glob.glob(path_to_images + '*')
path_to_classes = '/home/zhuhaozhe/data/L2/images_background/'
L2b = glob.glob(path_to_classes + '*')
all_classes += glob.glob(path_to_classes + '*')
for c in os.listdir(path_to_classes):
    path_to_images = os.path.join(path_to_classes, c) + '/'
    all_images += glob.glob(path_to_images + '*')
path_to_classes = '/home/zhuhaozhe/data/L2/images_evaluation/'
L2e = glob.glob(path_to_classes + '*')
all_classes += glob.glob(path_to_classes + '*')
for c in os.listdir(path_to_classes):
    path_to_images = os.path.join(path_to_classes, c) + '/'
    all_images += glob.glob(path_to_images + '*')

# Resize images
n = 0
for i, image_file in enumerate(all_images):
    try:
        im = Image.open(image_file)
        im = im.resize((84, 84), resample=Image.LANCZOS)
        im.save(image_file)
    except:
        print( "rm " + image_file)
        os.system("rm " + image_file)
        n += 1
        print("fail%d" % n)
    if i % 500 == 0:
        print(i)



# Put in correct directory
import random
random.shuffle(all_classes)
train = all_classes[:60]
val = all_classes[60:90]
test = all_classes[90:]
for datatype in ['train', 'val', 'test']:
    os.system('mkdir ' + datatype)
    classes = train if datatype == 'train' else val if datatype =='val' else test
    print(classes)
    for c in classes:
        image_dir = glob.glob(c + '/*')
        cur_dir = datatype + '/' + c.split('/')[-1] + '/'
        os.system('mkdir ' + cur_dir)
        for image in image_dir:
            os.system('cp ' + image + ' ' + cur_dir)

