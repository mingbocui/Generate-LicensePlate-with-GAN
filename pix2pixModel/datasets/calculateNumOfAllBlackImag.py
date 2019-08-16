from PIL import Image
import cv2
import os

dataPath = "/home/westwell/car_plate_dataset/A/old"
imagesList = os.listdir(dataPath)
i = 0
sum = 0
for imagPath in imagesList:
    img = cv2.imread(imagPath)
    if(cv2.countNonZero(img) == 0): i = i+1
    sum = sum+1

print(i/sum)