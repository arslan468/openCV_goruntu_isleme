import cv2

#kamerayı açıyoruz içinde ki sıfır değeri webcam den görüntü alınacağını belirtir
cap = cv2.VideoCapture(0)

#kameranın boyutlarını alıyoruz görüntüyü ona göre kaydedicez
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#kaydedilcek videonun adresini ve adını belirliyoruz
fileName = "/Users/mehmetalparslan/Desktop/github/openCV_goruntu_isleme/opencv_udemy/kaydedilen_videolar/webcam.mp4"
#mac için uygun formatlama türünü giriyoruz normalde 'm' 'p' '4' 'v' şeklinde kullanılır ama başına konulan * işareti bunu kısayoldan temsil ediyor
codec = cv2.VideoWriter_fourcc(*'mp4v')
#saniyede kaç kare olucağını belirler
frameRate = 30
# en ve boy bilgilerini bir değişkene aktarıyoruz 
resolution = (width,height)
#asıl işi yapan komut içindeki değişkenler sırasıyla kaydetme konumu, formatı, kare sayısı, ölçüleri
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution )
#while içine alıyoruz ki sürekli olarak gelen kareleri kaydedip video oluştursun
while True:
    #anlık olarak kamera da ki görüntüyü çeker ret ise kameranın açık olup olmama durumunu tutar true veya false döner ona göre bir kontrol sağlanabilir
    ret, frame = cap.read()
    #kameradan görüntü normalde ters olarak gelir bu satır gelen görüntüyü aynalar 1 yerine -1 girdiğimizde webcam baş aşağı görüntü getirir
    frame = cv2.flip(frame, 1)
    #anlık olarak kamera görüntüsünü ekrana basar
    cv2.imshow("Webcam Live", frame)
    #yukarıda belirlediğimiz adrese o anki görüntüyü yazar 
    videoFileOutput.write(frame)
    # 'q' ya basılınca döngüden çıkıp görüntü kaydetmeyi bitirmesi için 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

#kamerayı kapatır boşa çıkar
cap.release()
#videoyu bitirir bu komut önemlidir yoksa video bozuk olur 
videoFileOutput.release()
#webcam penceresini kapatır
cv2.destroyAllWindows()

