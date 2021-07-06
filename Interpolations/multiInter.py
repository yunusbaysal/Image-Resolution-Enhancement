from __future__ import division
import cv2
import numpy as np
import math
import sys, time
import os
import xlsxwriter
from skimage.metrics import structural_similarity as ssim

# excel files open
similarity = xlsxwriter.Workbook('similarityInterPolations.xlsx')
similarity1 = similarity.add_worksheet()
MSE1 = similarity.add_worksheet()


def mse(imageA, imageB):
    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
    err = err / float(imageA.shape[0] * imageA.shape[1])
    return err


# comparint
def compare_images(imageA, imageB, title, nameA, num, column):
    print("comparing...")
    # compute the mean squared error and structural similarity
    # index for the images

    # extract height, width and no. of channels from
    # original img
    h, w, c = imageA.shape
    hb, wb, cb = imageB.shape
    # i added try exception here
    # because some of colored images have 4 channels in
    # original one, and 3 in the upscaled ones
    # so in the mid of the process, it breaks the program, and
    # then i have to do every thing again
    # i thoght try0 except is helpful 
    try:
        if (h != hb or w != wb):
            h, w, c = imageA.shape
            print(imageB.shape)

            imgSize = (w, h)
            imageB = cv2.resize(imageB, imgSize)
            print(imageA.shape)

        s = ssim(imageA, imageB, multichannel=True)
        m = mse(imageA, imageB)
    except:
        print("image size could not fixed")
        return

    # to write on the sheets
    similarity1.write(num, 0, nameA)
    similarity1.write(num, column, s * 100)
    MSE1.write(num, 0, nameA)
    MSE1.write(num, column, m / 100)

    # print(title,s*100,nameA)


path = './LR'
print("Loading...")


def loadImages(path):
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.png')]


filenames = loadImages(path)
images = []
file_paths = []

print("loading Images...")
for file in filenames:
    images.append(cv2.imread(file, cv2.IMREAD_UNCHANGED))
    file_paths.append(os.path.basename(file))

original = loadImages('./pictures')

origImages = []
originalFile_paths = []
print("loading original...")

for file in original:
    origImages.append(cv2.imread(file, cv2.IMREAD_UNCHANGED))
    originalFile_paths.append(os.path.basename(file))

num = 0
for img in images:
    print("interpolation function")
    print(file_paths[num])
    h, w, c = img.shape
    ratio = 2
    height, weidth, c = origImages[num].shape
    imgSize = (weidth, height)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bilinear = cv2.resize(img, imgSize, interpolation=cv2.INTER_LINEAR)
    area = cv2.resize(img, imgSize, interpolation=cv2.INTER_AREA)
    bicubic = cv2.resize(img, imgSize, interpolation=cv2.INTER_CUBIC)
    nearest = cv2.resize(img, imgSize, interpolation=cv2.INTER_NEAREST)
    lanczos = cv2.resize(img, imgSize, interpolation=cv2.INTER_LANCZOS4)

    # to keep the resized images in hand
    cv2.imwrite("./bilinear/"+file_paths[num],bilinear)
    cv2.imwrite("./area/"+file_paths[num],area)
    cv2.imwrite("./bicubic/"+file_paths[num],bicubic)
    cv2.imwrite("./nearest/"+file_paths[num],nearest)
    cv2.imwrite("./lanczos/"+file_paths[num],lanczos)

    # sending the images to be compared
    compare_images(origImages[num], origImages[num], "Original vs. Original", file_paths[num], num, 1)
    compare_images(origImages[num],bilinear,"Original vs. Bilinear",file_paths[num],num,2)
    compare_images(origImages[num],area,"Original vs. area",file_paths[num],num,3)
    compare_images(origImages[num], bicubic, "Original vs. Bicubic", file_paths[num], num, 4)
    compare_images(origImages[num],nearest,"Original vs. Nearest-Neighbour",file_paths[num],num,5)
    compare_images(origImages[num], lanczos, "Original vs. Lanczos", file_paths[num], num, 6)

    num = num + 1

del origImages
del images

similarity.close()
