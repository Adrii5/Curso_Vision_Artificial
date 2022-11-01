import cv2
img = cv2.imread('nina.jpg',1)
tamano = img.size
alto,ancho,canales=img.shape
tipo=img.dtype
print("Tamaño: "+str(tamano)+" bytes")
print("Alto: "+str(alto)+" Pixeles")
print("Ancho: "+str(ancho)+" Pixeles")
print("Canales: "+str(canales)+" canales")
print("Tipo: "+str(tipo))
cv2.waitKey(0)
