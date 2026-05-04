import cv2
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)
parlakliklar = []

print("30 kare alınıyor... Bekle")

for _ in range(30):
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        ort = np.mean(gray)
        parlakliklar.append(ort)

cap.release()

# Sonuçları çiz
plt.figure(figsize=(10, 4))
plt.plot(parlakliklar, color='orange',
         linewidth=2, marker='o')
plt.title("Ortalama Parlaklık (30 Kare)")
plt.xlabel("Kare")
plt.ylabel("Ortalama Piksel Değeri")
plt.ylim(0, 255)
plt.grid(True, alpha=0.3)
plt.show()