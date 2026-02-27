import cv2
import numpy as np

img = np.zeros((100,30,3), dtype=np.uint8)




cv2.resize(img, (1000,1000), interpolation=cv2.INTER_AREA)
cv2.imshow("Canvas", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

