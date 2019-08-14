import numpy as np
import os
import glob
import cv2

data_path = "/home/westwell/car_plate_dataset/B/old"
path = os.path.join(data_path, '*')
images_path = glob.glob(path)
#print(images_path[:10])
#images_path = images_path[:10]
write_path = "/home/westwell/car_plate_dataset/A/old"

images_path = sorted(images_path)

for image_path in images_path:
    image_name = image_path.split("/")[-1]

    #print(image_name)
    image = cv2.imread(image_path,0)
    final_path = os.path.join(write_path,image_name)
    cv2.imwrite(final_path, cv2.Canny(image, 120, 120))