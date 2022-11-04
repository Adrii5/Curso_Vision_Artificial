import cv2

img1 = cv2.imread("Estrellas.jpg",1)
img2=cv2.imread("Planeta.jpg",1)

ancho = int(236)
alto = int(419)
img2_rescalado = cv2.resize(img2,(ancho,alto))



img3 = cv2.addWeighted(img1,0.9,img2_rescalado,0.9,0)



cv2.imshow("Estrellas",img3)

key = cv2.waitKey(0)