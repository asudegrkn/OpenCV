
import cv2

img = cv2.imread("lenna.png" , 0)

cv2.imshow("orijinal",img)

#resized
imgResized= cv2.resize(img , (800,800))
print("Resized Img Shape:", imgResized.shape)
cv2.imshow("img resized" , imgResized)

#kırp
imgCropped = img[:200,0:300] #yükesklik-genişlik (y,x)
cv2.imshow("kirpilmis resim", imgCropped)

