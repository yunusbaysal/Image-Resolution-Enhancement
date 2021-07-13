import cv2
import numpy as np
from math import sqrt,exp
import FilterFunctions as filterPass

def lowPassFilters(img, fileName,orderValue):
    original = np.fft.fft2(img)
    center = np.fft.fftshift(original)
    
    if orderValue == 1:
        LowPassCenter = center * filterPass.idealFilterLP(50,img.shape)
        LowPass = np.fft.ifftshift(LowPassCenter)
        inverse_LowPass = np.fft.ifft2(LowPass)
        new_result=np.abs(inverse_LowPass)
        
        cv2.imwrite('./IdealLow/'+'Input'+fileName,img)
        cv2.imwrite('./IdealLow/'+fileName,new_result)
    elif orderValue == 2:
        LowPassCenter = center * filterPass.butterworthLP(50,img.shape,10)    #n = 10 girildi
        LowPass = np.fft.ifftshift(LowPassCenter)
        inverse_LowPass = np.fft.ifft2(LowPass)
        new_result = np.abs(inverse_LowPass)
        
        cv2.imwrite('./ButterworthLow/'+'Input'+fileName,img)
        cv2.imwrite('./ButterworthLow/'+fileName,new_result)
    elif orderValue == 3:
        LowPassCenter = center * filterPass.gaussianLP(50,img.shape)
        LowPass = np.fft.ifftshift(LowPassCenter)
        inverse_LowPass = np.fft.ifft2(LowPass)
        new_result =np.abs(inverse_LowPass)
        
        cv2.imwrite('./GaussianLow/'+'Input'+fileName,img)
        cv2.imwrite('./GaussianLow/'+fileName,new_result)
    
    return new_result

def highPassFilters(img, fileName,orderValue):
    original = np.fft.fft2(img)
    center = np.fft.fftshift(original)
    
    if orderValue == 1:
        HighPassCenter = center * filterPass.idealFilterHP(50,img.shape)
        HighPass = np.fft.ifftshift(HighPassCenter)
        inverse_HighPass = np.fft.ifft2(HighPass)
        new_result = np.abs(inverse_HighPass)
        
        cv2.imwrite('./IdealHigh/'+'Input'+fileName,img)
        cv2.imwrite('./IdealHigh/'+fileName,new_result)
    elif orderValue == 2:
        HighPassCenter = center * filterPass.butterworthHP(50,img.shape,10)
        HighPass = np.fft.ifftshift(HighPassCenter)
        inverse_HighPass = np.fft.ifft2(HighPass)
        new_result = np.abs(inverse_HighPass)
        
        cv2.imwrite('./ButterworthHigh/'+'Input'+fileName,img)
        cv2.imwrite('./ButterworthHigh/'+fileName,new_result)
    elif orderValue == 3:
        HighPassCenter = center * filterPass.gaussianHP(50,img.shape)
        HighPass = np.fft.ifftshift(HighPassCenter)
        inverse_HighPass = np.fft.ifft2(HighPass)
        new_result = np.abs(inverse_HighPass)
        
        cv2.imwrite('./GaussianHigh/'+'Input'+fileName,img)
        cv2.imwrite('./GaussianHigh/'+fileName,new_result)
        
    return new_result
