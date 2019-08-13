#coding=utf-8
import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
import cv2;
import numpy as np;
import os;
from math import *


# font = ImageFont.truetype("Arial-Bold.ttf",14)

index = {"京": 0, "沪": 1, "津": 2, "渝": 3, "冀": 4, "晋": 5, "蒙": 6, "辽": 7, "吉": 8, "黑": 9, "苏": 10, "浙": 11, "皖": 12,
         "闽": 13, "赣": 14, "鲁": 15, "豫": 16, "鄂": 17, "湘": 18, "粤": 19, "桂": 20, "琼": 21, "川": 22, "贵": 23, "云": 24,
         "藏": 25, "陕": 26, "甘": 27, "青": 28, "宁": 29, "新": 30, "0": 31, "1": 32, "2": 33, "3": 34, "4": 35, "5": 36,
         "6": 37, "7": 38, "8": 39, "9": 40, "A": 41, "B": 42, "C": 43, "D": 44, "E": 45, "F": 46, "G": 47, "H": 48,
         "J": 49, "K": 50, "L": 51, "M": 52, "N": 53, "P": 54, "Q": 55, "R": 56, "S": 57, "T": 58, "U": 59, "V": 60,
         "W": 61, "X": 62, "Y": 63, "Z": 64};

chars = ["京", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "皖", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂",
             "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A",
             "B", "C", "D", "E", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
             "Y", "Z"
             ];

def GenCh(f,val):
    img=Image.new("RGB", (45,70),(255,255,255))
    draw = ImageDraw.Draw(img)
    draw.text((0, 3),val,(0,0,0),font=f)
    img =  img.resize((23,70))
    A = np.array(img)

    return A

def GenCh1(f,val):
    img=Image.new("RGB", (23,70),(255,255,255))
    draw = ImageDraw.Draw(img)
    # draw.text((0, 2),val.decode('utf-8'),(0,0,0),font=f)
    draw.text((0, 2), val, (0, 0, 0), font=f)
    A = np.array(img)
    return A



def r(val):
    return int(np.random.random() * val)



class GenPlate:


    def __init__(self,fontCh,fontEng,NoPlates):
        self.fontC =  ImageFont.truetype(fontCh,43,0);
        self.fontE =  ImageFont.truetype(fontEng,60,0);
        self.img=np.array(Image.new("RGB", (226,70),(255,255,255)))
        self.bg  = cv2.resize(cv2.imread("./images/template.bmp"),(226,70));
        self.smu = cv2.imread("./images/smu2.jpg");
        self.noplates_path = [];
        for parent,parent_folder,filenames in os.walk(NoPlates):
            for filename in filenames:
                path = parent+"/"+filename;
                self.noplates_path.append(path);


    def draw(self,val):
        offset= 2 ;

        self.img[0:70,offset+8:offset+8+23]= GenCh(self.fontC,val[0]);
        self.img[0:70,offset+8+23+6:offset+8+23+6+23]= GenCh1(self.fontE,val[1]);
        for i in range(5):
            base = offset+8+23+6+23+17 +i*23 + i*6 ;
            self.img[0:70, base  : base+23]= GenCh1(self.fontE,val[i+2]);
        return self.img

    def generate(self,text):

            fg = self.draw(text);

            fg = cv2.bitwise_not(fg);
            com = cv2.bitwise_or(fg,self.bg);


            return com

    def genPlateString(self,pos,val):
        plateStr = "";
        box = [0,0,0,0,0,0,0];
        if(pos!=-1):
            box[pos]=1;
        for unit,cpos in zip(box,range(len(box))):
            if unit == 1:
                plateStr += val
            else:
                if cpos == 0:
                    plateStr += chars[r(31)]
                elif cpos == 1:
                    plateStr += chars[41+r(24)]
                else:
                    plateStr += chars[31 + r(34)]

        return plateStr;

    def genBatch(self, batchSize,pos,charRange, outputPath,size):
        if (not os.path.exists(outputPath)):
            os.mkdir(outputPath)
        for i in range(batchSize):
            plateStr = G.genPlateString(-1,-1)

            img =  G.generate(plateStr);

            filename = os.path.join(outputPath, str(i).zfill(4) + '-' + plateStr + ".jpg")
            cv2.imwrite(filename, img);

if __name__ == '__main__':

    G = GenPlate("./font/platech.ttf",'./font/platechar.ttf',"./NoPlates")

    G.genBatch(100,2,range(31,65),"./plate_test",(272,72))

