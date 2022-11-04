import cv2

img  = cv2.imread("Notredame.jpg",1)

alto,ancho,_ = img.shape
escala = 0.5

ancho_escalado,alto_escalado = int(ancho*escala),int(alto*escala)

imagen_escala = cv2.resize(img,(ancho_escalado,alto_escalado))

cv2.imshow("Imagen Original",img)
cv2.imshow("Imagen Escalada",imagen_escala)

cv2.waitKey(0)
cv2.destroyAllWindows()