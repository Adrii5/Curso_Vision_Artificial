import cv2
img = cv2.imread("nina.jpg",1)
alto, ancho, _ = img.shape
color=(0,0,255)
grosor = 2
cuadricula = 2

for x in range(0,ancho+1,cuadricula):
    img = cv2.line(img,(x,0),(x,alto),color,ancho)
for y in range(0,alto+1,cuadricula):
    img = cv2.line(img,(0,y),(ancho,y),color,grosor)

cv2.namedWindow("Cuadro",cv2.WINDOW_NORMAL)
cv2.imshow("Cuadro",img)
cv2.waitKey(0)
