import cv2

#kamerayı açıyoruz
cap = cv2.VideoCapture(0)

#kameranın boyutlarını alıyoruz görüntüyü ona göre kaydedicez
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) 
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#kaydedilcek videonun adresini ve adını belirliyoruz
fileName = "/Users/mehmetalparslan/Desktop/github/openCV_goruntu_isleme/opencv_udemy/kaydedilen_videolar/webcam.mp4"
#mac için uygun codec giriyoruz
codec = cv2.VideoWriter_fourcc(*'mp4v')
frameRate = 30
resolution = (width,height)
videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution )

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    cv2.imshow("Webcam Live", frame)
    videoFileOutput.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
videoFileOutput.release()
cv2.destroyAllWindows()










