import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

path = "/Users/mehmetalparslan/Desktop/github/openCV_goruntu_isleme/opencv_udemy/gorseller/openCV_Logo.png"
img = cv2.imread(path)
width, height, _ = img.shape

print("Image[Width: {}, Height: {}]".format(width, height))
#(b,g,r) = img[200,100]

#print("(50, 30) - Red: {}, Green: {}, Blue {}".format(r,g,b))

print("======BAŞLIYOR=======")
print("--------------------------------------")
for i in range(width):
    for j in range(height):
        (b,g,r) = img[i,j]
        print("Image[{},{}] - Red: {}, Green: {}, Blue: {}".format(i,j,r,g,b))



#terminale yazıldığında çıktıyı txt olarak dosyaya kaydeder
#python 00_pixel_operations.py > rapor.txt 
