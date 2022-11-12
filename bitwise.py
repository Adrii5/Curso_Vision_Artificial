#se importa la libreria open cv
import cv2
#se cargan las imagenes 
img1 = cv2.imread("nina.jpg",1)
img2 = cv2.imread("isabel.jpg",1)
#La img2 es muy grande, se rescala 
img2 = cv2.resize(img2,(150,75))
# de img2 se saca el alto y ancho de la imagen 
#real ente no es necesiario ya que 
#en este caso nosotron introducomos esos datos 
alto,ancho,_=img2.shape
#Del cuadro de nina se estrae el area en la 
#que vamos a colocar las letras, en este caso es la esquina 
#superior hizquierda
area_trabajo = img1[0:alto,0:ancho]
#ya que se tienen extraida el area de trabajo del cuadro de nina 
#y las letras que vamos a agregar a esa area, se hace la operacion 
#bit  a bit (bitwise), seria algo como combienar esas dos imagenes 
#ya que se comninan, se guarda la nueva imagen combinada en una variable n
n=cv2.bitwise_and(img2,area_trabajo)
#ahora se agrega el pedaso que se le quito a la imagen de nina 
#pero se cambia por el nuevo pedazo combinado
img1[0:alto,0:ancho]=n
#listo, solo se muestra la imagen 
cv2.imshow("Niña",img1)


key = cv2.waitKey(0)