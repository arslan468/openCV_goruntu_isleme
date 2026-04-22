import cv2
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
ret, frame = cap.read()

if ret:
    # OpenCV BGR'yi RGB'ye çevir
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(frame_rgb)
    plt.title("Kamera Görüntüsü")
    plt.axis('off')
    plt.show()

cap.release()