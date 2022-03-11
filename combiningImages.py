import cv2
import numpy as np

#resmi içe aktar
img = cv2.imread("lenna.png")
cv2.imshow("orijinal",img)

#yanyana
hor = np.hstack((img,img))
cv2.imshow("yatay",hor)


#dikey
ver=np.vstack((img,img))
cv2.imshow("dikey",ver)

k = cv2.waitKey(0) & 0xFF

if k == 27: #esc
    cv2.destroyAllWindows() 