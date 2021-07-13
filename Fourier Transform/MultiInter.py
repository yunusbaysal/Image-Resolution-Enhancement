from __future__ import division
import cv2
import numpy as np
import math
import sys, time
import os
import Comparison_Images as Mymodule
import InterpolationsWithChannelConvert as MyInter
import UnitTest
import xlsxwriter
import FastFourierTransform  as FFTransform
# For Input Data
path ="./resized"
def loadImages(path):
    print("Loading...")
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]

#For Original Data
path2 ="./pictures"
def loadImages2(path2):
    print("Loading...")
    return [os.path.join(path2,f) for f in os.listdir(path2) if f.endswith('.jpg')]

filenames = loadImages(path)
images = []
file_paths = []
Dictionary = dict()

for file in filenames:
    print("loading Input Images...")
    images.append(cv2.imread(file,cv2.IMREAD_UNCHANGED))
    file_paths.append(os.path.basename(file))
    
filenames2 = loadImages2(path2)
imagesOrg = list()
dictionaryData =dict()

for file in filenames2:
    print("loading Original Images...")
    imagesOrg.append(cv2.imread(file,cv2.IMREAD_UNCHANGED))

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('./GaussianHigh/DataMSE_CurrentTermGaussianHigh.xlsx')
worksheet = workbook.add_worksheet()

# Add a bold format to use to highlight cells.
bold = workbook.add_format({'bold': 1})

# Write some data headers.
worksheet.write('A1', 'Image Name', bold)
worksheet.write('B1', 'Bilinear', bold)
worksheet.write('C1', 'Area', bold)
worksheet.write('D1', 'Bicubic', bold)
worksheet.write('E1', 'Nearest(NN)', bold)
worksheet.write('F1', 'Lanczos', bold)

# Start from the first cell below the headers.
row = 1
col = 0

# Buraya input ve original data verilerinin sayısının eşit olduğuna dair bir if yazılıp tüm işlemler bu if içinde olacak!
if len(images) == len(imagesOrg):
    num=0 
    for img in images:
        print("-----------------------------------------------------------------------------------")
        print("In:"+str(img.shape[0])+"  "+str(img.shape[1]))
        print("Org:"+str((imagesOrg[num]).shape[0])+"  "+str((imagesOrg[num]).shape[1]))
        imgSize= Mymodule.Image_size(img,imagesOrg[num])
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        #print(file_paths[num])
        #img = FFTransform.lowPassFilters(img,file_paths[num],3)
        img = FFTransform.highPassFilters(img,file_paths[num],3)
        
        bilinear = MyInter.Bilinear_Inter(img,imgSize)
        area = MyInter.Area_Inter(img,imgSize)
        bicubic = MyInter.Bicubic_Inter(img,imgSize) 
        nearest = MyInter.NN_Inter(img,imgSize)
        lanczos  = MyInter.Lanczos_Inter(img,imgSize)
        
        imagesOrg[num] = cv2.cvtColor(imagesOrg[num], cv2.COLOR_BGR2GRAY)
        #Unit Test Step
        #if (UnitTest.UnitTestProcesses(imagesOrg[num],bilinear,area,bicubic,nearest,lanczos)):
        #önce height sonra widt, ve interpolations
        temp_list =[bilinear.shape[0],bilinear.shape[1],Mymodule.mse(imagesOrg[num],bilinear),
                        Mymodule.mse(imagesOrg[num],area),
                        Mymodule.mse(imagesOrg[num],bicubic),
                        Mymodule.mse(imagesOrg[num],nearest),
                        Mymodule.mse(imagesOrg[num],lanczos)
                        ]
        worksheet.write_string(row,col,file_paths[num])
        worksheet.write_number(row, col + 1,temp_list[2])
        worksheet.write_number(row, col + 2,temp_list[3])
        worksheet.write_number(row, col + 3,temp_list[4])
        worksheet.write_number(row, col + 4,temp_list[5])
        worksheet.write_number(row, col + 5,temp_list[6])
        
        Dictionary[file_paths[num]] = temp_list
        #else:
        #    print("Unit Test Error!")
        #    break
        
        num =num + 1
        row =row + 1

    #print(Dictionary)
else :
    print("Error! It is not equal sizes of Resized and Pictures files")
    
workbook.close()