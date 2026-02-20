import cv2

img = cv2.imread("klon.jpg")
print(img)

img = cv2.resize(img, (640,480))

cv2.imshow("Resim", img)


cv2.waitKey(0)

cv2.destroyAllWindows()