import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fileName = "/Users/mehmetalparslan/Desktop/github/openCV_goruntu_isleme/opencv_udemy/kaydedilen_videolar/tekrar.mp4"

codec = cv2.VideoWriter_fourcc(*'mp4v')

frameRate= 30

resolution = (width,height)

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

while True:

    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.imshow("Tekrar_kayıt", frame)
    videoFileOutput.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
videoFileOutput.release
cv2.destroyAllWindows()







"""

import cv2

img = cv2.imread("klon.jpg")

# Önce resmin boyunu posunu alalım
# img.shape bize (Yükseklik, Genişlik, Kanal) verir
h, w, channels = img.shape 

print(f"Resim Boyutu: {h}x{w}") # Mesela 300x400 yazar

# Döngüyü kurarken sayıyı elle yazma, 'h' (yükseklik) değişkenini kullan.
# range(h) demek: 0'dan başla, h'ye KADAR git (h dahil değil).
# Yani h=300 ise, 0...299 yapar. Tam bizim istediğimiz!

for i in range(h): # Yükseklik (Satırlar)
    for j in range(w): # Genişlik (Sütunlar)
        # Artık i asla 300 olmaz, en fazla 299 olur.
        (b, g, r) = img[i, j] 
        
        # Buraya işlemini yaz...
        # Mesela pikselleri kırmızı yapalım:
        # img[i, j] = (0, 0, 255)

print("İşlem tamam gardaş, kimse yere düşmedi!")




"""