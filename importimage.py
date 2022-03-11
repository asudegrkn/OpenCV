
import cv2

##içe aktarma

img = cv2.imread("rengoku.jpg", 0)

#görselleştir
cv2.imshow("ilk resim", img)

k = cv2.waitKey(0) &0xFF

if k == 27: #esc
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("rengoku_gray.png", img)
    cv2.destroyAllWindows()
