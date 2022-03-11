import cv2

import numpy as np

img = cv2.imread("kart.png"  )
cv2.imshow("kart",img)

width = 400
height = 500

#◘yamuk resmin kordinaatları
pts1 = np.float32([[203,2],[4,473],[538,147],[339,617]])
pts2= np.float32([[0,0],[0,height],[0,width],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
print(matrix)

#nihai dönüştürülmüş resim
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("son resim",imgOutput)

k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
    