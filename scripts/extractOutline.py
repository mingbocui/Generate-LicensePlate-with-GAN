import numpy as np
import os
import glob
import cv2

import argparse

def extract(data_path, write_path):

    path = os.path.join(data_path, '*')
    images_path = glob.glob(path)

    images_path = sorted(images_path)

    for image_path in images_path:
        image_name = image_path.split("/")[-1]

        #print(image_name)
        image = cv2.imread(image_path,0)
        final_path = os.path.join(write_path,image_name)
        cv2.imwrite(final_path, cv2.Canny(image, 120, 120))

if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--A_path', default=None, help='path where you wan to store the outline image')
    parser.add_argument('--B_path', default=None, help='path of the original image')
    args = parser.parse_args()

    extract(args.B_path, args.A_path)