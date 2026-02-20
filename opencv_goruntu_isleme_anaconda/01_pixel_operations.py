import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

path = "/Users/mehmetalparslan/Desktop/github/openCV_goruntu_isleme/opencv_udemy/gorseller/openCV_Logo.png"

img = cv2.imread(path)

width, height , _ = img.shape

for i in range(width):
    for j in range(height):
        (b,g,r) = img[i,j]
        if b != 255 or g !=255 or r != 255:
            print("Image[{},{}] - Red: {}, Green: {}, Blue: {}".format(i,j,r,g,b))
                



#terminale yazıldığında çıktıyı txt olarak dosyaya kaydeder
#python 01_pixel_operations.py > renkli.txt 
