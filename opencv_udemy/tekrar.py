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