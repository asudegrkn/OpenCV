import cv2

#capture
cap=cv2.VideoCapture(0) #default cam harici cam-(1)


width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width,height)


# video kaydet 
writer = cv2.VideoWriter("video_kaydi.mp4", cv2.VideoWriter_fourcc(*'DIVX'),20,(width,height))

"""
*video_kaydi.mp4 --> kaydedilen video dosya ismi
**fourcc("DIVX")  windows için / çerçeveleri sıkıştırmak için kullanılan 4 karakterli codec  
**FourCC nin amacı medya verilerindeki codec’leri dört karakter ile tanımlamaktır
*** frame persecond 20 = video akış hızı her saniyede göreceğimiz frame (resim) sayısı
"""

while True:
    ret, frame = cap.read() #video camden gelecek resimlerin her birini read olarak her bir frame aktarıyor  freamin gelip gelmediğini de ret içerisine aktarıyo  
    
    cv2.imshow("Video", frame) #videoyu göster
    
    #save
    writer.write(frame )
    
    if cv2.waitKey(1) & 0xFF == ord("q"): break

cap.release()
writer.release()
cv2.destroyAllWindows()