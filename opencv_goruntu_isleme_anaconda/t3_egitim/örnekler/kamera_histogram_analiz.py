import cv2
import matplotlib.pyplot as plt

img = cv2.imread("resim.jpg")

renkler = ('b', 'g', 'r')
isimler = ('Mavi', 'Yeşil', 'Kırmızı')

plt.figure(figsize=(10, 4))

for i, (renk, isim) in enumerate(zip(renkler, isimler)):
    hist = cv2.calcHist([img], [i], None,
                          [256], [0,256])
    plt.plot(hist, color=renk, label=isim)

plt.legend()
plt.title("Renk Histogramı")
plt.xlim([0, 256])
plt.show()