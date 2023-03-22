from PIL import Image
from PIL.TiffTags import TAGS
import re
import rasterio
import rasterio.features
import rasterio.warp
import numpy as np 
import cv2
import imutils
import matplotlib.pyplot as plt
import glob

patron = "*DJI_*[0-9]*"
archivos_encontrados = glob.glob("Img" + "/" + patron)

print("Archivos encontrados:")
for img_path in archivos_encontrados:
    img_path = "Img/DJI_0041.TIF" 
    img_rect_path = "Img_rectificada/"
    img_rot_path = "Img_rotado/"    
    img_rot_TIF_path = "Img_rotado_TIF/" 

    n_imagen = img_path.split("/")[-1]
    n_imagen = n_imagen.split(".")[0]
    print(n_imagen)

    n_esima = n_imagen.split("_")[-1]
    print(n_esima)

    img_rot_path = img_rot_path + n_imagen + "_rot0.PNG"
    img_rect_path = img_rect_path + n_imagen + "_rect0.PNG"
    img_rot_TIF_path = img_rot_TIF_path +n_imagen + "TIF_rot0.TIF"

    print(img_rot_TIF_path)
    print(img_rot_path)
    print(img_rect_path)
