import cv2
import numpy as np
import requests

url = "http://192.168.1.105:8080//shot.jpg"
fileName = "/Users/mehmetalparslan/Desktop/github/openCV_goruntu_isleme/opencv_udemy/kaydedilen_videolar/tabletten_gelen_goruntu.mp4"

img_resp = requests.get(url)
img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

height, width, _ = img.shape
resolution = (width,height)


frameRate = 30
codec = cv2.VideoWriter_fourcc(*'mp4v')
height, width, channels = img.shape

videoFileOutput = cv2.VideoWriter(fileName,codec ,frameRate, resolution)

while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)


    videoFileOutput.write(img)
    cv2.imshow("Android Camera", img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
videoFileOutput.release()














"""
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fileName = "/Users/mehmetalparslan/Desktop/github/openCV_goruntu_isleme/opencv_udemy/kaydedilen_videolar/andorid_cihaz.mp4"

codec = cv2.VideoWriter_fourcc(*'mp4v')

frameRate = 30
resolution = (width, height)

videoFileOutput = cv2.VideoWriter(fileName, codec, frameRate, resolution)

while True:
    ret, frame = cap.read()

    frame = cv2.flip(frame, 1)

    cv2.imshow("Webcam Live", frame)
    videoFileOutput.write(frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
videoFileOutput.release()
cv2.destroyAllWindows()"""