import cv2
import numpy as np 
from matplotlib import pyplot as plt
from skimage.metrics import structural_similarity as ssim
import math

def Image_size(img,imgOr):
    
    print("interpolation function")
    h,w,c= img.shape
    ratio=1/0.7
    w = math.floor(w* ratio)
    h= math.floor(h*ratio)
    if(imgOr.shape[1] == w):
        pass
    else:
        print("Old width  : "+str(w))
        w = imgOr.shape[1]
        print("New width  : "+str(w))
    
    if(imgOr.shape[0] == h):
        pass
    else:
        print("Old Height  : "+str(h))
        h=imgOr.shape[0]
        print("New Height  : "+str(h))
    
    imgSize= (w,h)
    return imgSize

def mse(imageA, imageB):
    # the 'Mean Squared Error' between the two images is the
    # sum of the squared difference between the two images;
    # NOTE: the two images must have the same dimension
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err /= float(imageA.shape[0] * imageA.shape[1])

    # return the MSE, the lower the error, the more "similar"
    # the two images are
    err = err / 100.0
    return err
