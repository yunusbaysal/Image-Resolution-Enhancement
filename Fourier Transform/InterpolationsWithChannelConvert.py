import cv2

# For Bilinear Interpolations, return Grayscale type
def Bilinear_Inter(img, imgSize):
    img = cv2.resize(img, imgSize, interpolation=cv2.INTER_LINEAR)
    print("Bil:"+str(img.shape[0])+"  "+str(img.shape[1]))
    return img

# For Area Interpolations, return Grayscale type
def Area_Inter(img, imgSize):
    img = cv2.resize(img, imgSize, interpolation=cv2.INTER_AREA)
    print("Area:"+str(img.shape[0])+"  "+str(img.shape[1]))
    return img

# For Bicubic Interpolations, return Grayscale type
def Bicubic_Inter(img, imgSize):
    img = cv2.resize(img, imgSize, interpolation=cv2.INTER_CUBIC)
    print("Bic:"+str(img.shape[0])+"  "+str(img.shape[1]))
    return img

# For Nearest Neighbour Interpolations, return Grayscale type
def NN_Inter(img, imgSize):
    img = cv2.resize(img, imgSize, interpolation=cv2.INTER_NEAREST)
    print("NN:"+str(img.shape[0])+"  "+str(img.shape[1]))
    return img

# For Lanczos Interpolations, return Grayscale type
def Lanczos_Inter(img, imgSize):
    img = cv2.resize(img, imgSize, interpolation=cv2.INTER_LANCZOS4)
    print("Lanc:"+str(img.shape[0])+"  "+str(img.shape[1]))
    return img