# -*- coding: utf-8 -*-
"""
Created on Mon Apr 02 21:03:44 2018
@author: Fsl
"""
import shutil
import os
import glob
import random
import math
import argparse

def write(imgs_list, fileObject):
    for img_name in imgs_list:
        fileObject.write(img_name)
        fileObject.write('\n')

    fileObject.close()



def objFileName(rootPath):

    # data_path = "/home/westwell/car_plate_dataset/B"
    # path = os.path.join(data_path, '*')
    # images_path = glob.glob(path)
    # images_path = sorted(images_path
    #
    # images_name = images_path.split("/")[-1]

    images_name = os.listdir(rootPath+'/old/')

    numImg = len(images_name)

    ratioTrain = 0.7
    ratioVal = 0.2
    ratioTest = 0.1

    random.shuffle(images_name)
    train_image = images_name[ : math.floor(ratioTrain*numImg)]
    val_image = images_name[math.floor(ratioTrain*numImg) : math.floor(ratioTrain*numImg)+math.floor(ratioVal * numImg)]
    test_image = images_name[-math.floor(ratioTest * numImg):]

    # trainFile = open("/home/westwell/car_plate_dataset/train.txt", 'w')
    # testFile = open("/home/westwell/car_plate_dataset/test.txt", 'w')
    # valFile = open("/home/westwell/car_plate_dataset/val.txt", 'w')
    #
    # write(train_image, trainFile)
    # write(test_image, testFile)
    # write(val_image, valFile)

    return train_image, val_image, test_image

def copy(list, sourcePath, destinationPath):
    for img in list:
        shutil.copy(sourcePath+'/'+img, destinationPath+'/'+img)


def copy_img(rootPath):
    "/home/westwell/car_plate_dataset/B/old/"
    train_image, val_image, test_image = objFileName(rootPath+'/B/')

    copy(train_image, rootPath+'/B/old/', rootPath+'/B/train/')
    copy(val_image, rootPath+'/B/old/', rootPath+'/B/val/')
    copy(test_image, rootPath+'/B/old/', rootPath+'/B/test/')

    copy(train_image, rootPath+'/A/old/', rootPath+'/A/train/')
    copy(val_image, rootPath+'/A/old/', rootPath+'/A/val/')
    copy(test_image, rootPath+'/A/old/', rootPath+'/A/test/')



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default=None, help='rootPath')
    args = parser.parse_args()

    if args.path is not None:
        copy_img(args.path)
    else:
        rootPath = "/home/westwell/car_plate_dataset"
        copy_img(rootPath)