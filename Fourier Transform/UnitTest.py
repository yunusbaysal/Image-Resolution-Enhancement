import cv2
import Comparison_Images as Mymodule

def UnitTestProcesses(ImageOr,bilinear,area,bicubic,nearest,lanczos):
    flag = True
    check = list()
    check.append(Mymodule.mse(ImageOr,ImageOr))
    check.append(Mymodule.mse(bilinear,bilinear))
    check.append(Mymodule.mse(area,area))
    check.append(Mymodule.mse(bicubic,bicubic))
    check.append(Mymodule.mse(nearest,nearest))
    check.append(Mymodule.mse(lanczos,lanczos))
    
    #mse değerleri sıfır dışında farklı bir sonuc verirse hata vermeli!
    for i in check:
        if i != 0:
            flag = False
            break
    return flag