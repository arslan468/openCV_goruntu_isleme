import cv2
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

path = "/Users/mehmetalparslan/Desktop/github/openCV_goruntu_isleme/opencv_udemy/gorseller/klon.jpg"

img = cv2.imread(path)

width, height , _ = img.shape

corner = img[0:170, 0:300] #[y-start:y-end, x-start:x-end]

cv2.imshow("Corner: ", corner)
cv2.imshow("img", img)

#verilen aralıkta ki pixellerin renk değerlerini değiştirme
img[0:170, 0:250] = (0,255,0) #b,g,r


cv2.imshow("Corner: ", corner)
cv2.imshow("img", img)


cv2.waitKey(0)
cv2.destroyAllWindows()




"""
for i in range(width):
    for j in range(height):
        (b,g,r) = img[i,j]
        if b != 255 or g !=255 or r != 255:
            print("Image[{},{}] - Red: {}, Green: {}, Blue: {}".format(i,j,r,g,b))
"""

#terminale yazıldığında çıktıyı txt olarak dosyaya kaydeder
#python 01_pixel_operations.py > renkli.txt 
