import cv2
import matplotlib.pyplot as plt

img = cv2.imread("resim.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Küçük bir bölge al (daha net görünür)
bolge = gray[0:100, 0:100]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))

ax1.imshow(bolge, cmap='gray')
ax1.set_title("Gri Görüntü")

im = ax2.imshow(bolge, cmap='plasma')
ax2.set_title("Piksel Isı Haritası")
plt.colorbar(im, ax=ax2)

plt.show()