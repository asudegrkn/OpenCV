import cv2

import numpy as np

#resim oluştur
img = np.zeros((512,512,3), np.uint8) #siyah resim
print(img.shape)

cv2.imshow("siyah", img)



#çizgi
# resim, başlangıç noktası, bitiş noktası, renk , kalınlık
cv2.line(img, (0,0) , (512,512), (0,255,0), 3) # BGR
cv2.imshow("cizgi",img)

#dikdörtgen
#resim,başlangıç,bitiş,renk
cv2.rectangle(img,(0,0),(256,256),(255,0,0), cv2.FILLED)#doldurulmuş
cv2.imshow("dikdortgen",img)


#çember
#resim,merkez,yarı çap ,rengi
cv2.circle(img, (300,300),45,(0,0,255), cv2. FILLED)
cv2.imshow("cember",img)

#metin
#resim,başlangıç noktası,font, kalınlığı,renk
cv2.putText(img,"resim",(350,350), cv2.FONT_HERSHEY_COMPLEX, 1,(255,255,255))
cv2.imshow("metin",img)

k = cv2.waitKey(0) & 0xFF

if k == 27: #esc
    cv2.destroyAllWindows() 