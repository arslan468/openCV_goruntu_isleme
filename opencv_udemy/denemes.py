import cv2
import numpy as np
import requests

url = "http://192.168.1.105:8080//shot.jpg"

# --- ADIM 1: Önce bi numune alıp boyunu posunu öğrenelim ---
print("Gardaş bi dur, kameradan ilk görüntüyü alıp ölçülerini bakıyom...")

try:
    # İlk resmi çek
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    initial_frame = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    # İşte aradığın ölçü alma olayı burda!
    # shape bize (Yükseklik, Genişlik, Kanal) verir.
    height, width, channels = initial_frame.shape
    print(f"Ölçüleri aldım gardaş! Genişlik: {width}, Yükseklik: {height}")

except Exception as e:
    print("La gardaş kamera cevap vermiyor, IP doğru mu?:", e)
    exit() # Hata varsa programı durdur

# --- ADIM 2: Video Kaydediciyi Hazırla ---
# Dosya yolunu kendine göre ayarla
fileName = "/Users/mehmetalparslan/Desktop/github/openCV_goruntu_isleme/opencv_udemy/kaydedilen_videolar/android_cihaz.mp4"

# Mac için kral codec: mp4v
codec = cv2.VideoWriter_fourcc(*'mp4v')
frameRate = 30
resolution = (width, height) # Bak yukarıda bulduğumuz ölçüyü buraya verdik

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

# Dosya oluştu mu kontrol et
if not videoFileOutput.isOpened():
    print("Video dosyası açılamadı, codec'e ya da dosya yoluna bi bak!")

print("Kayıt başladı aslanım, durdurmak için 'ESC' bas...")

# --- ADIM 3: Döngüyü Başlat ---
while True:
    try:
        # Sürekli yeni resim iste (Video akışı gibi)
        img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
        
        # Yeniden boyutlandırmaya gerek yok, zaten orjinal boyutu aldık.
        # Ama illa değiştirecem dersen: img = cv2.resize(img, (640, 480)) yapabilirsin.

        # Ekranda göster
        cv2.imshow("Android Camera", img)
        
        # Videoya kaydet
        videoFileOutput.write(img)

        # ESC (27) tuşuna basınca çık
        if cv2.waitKey(1) == 27:
            print("Kayıt bitti, dükkanı kapatıyoz.")
            break
            
    except Exception as e:
        print("Akış koptu gardaş:", e)
        break

# Temizlik imandan gelir
videoFileOutput.release()
cv2.destroyAllWindows()


