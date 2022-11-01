
                         #Ventanas
#import cv2
#img = cv2.imread("nina.jpg",1)

#cv2.namedWindow("Cuadro",cv2.WINDOW_NORMAL)
#cv2.moveWindow("Cuadro",0,0)
#cv2.imshow("Cuadro",img)

#cv2.waitKey(0)

                         #Lineas

#import cv2
#img = cv2.imread("nina.jpg",1)
#alto, ancho, _ = img.shape
#color =(0, 0, 255)
#grosor = 2
#cuadricula = 80

#for x in range(0, ancho+1, cuadricula):
#    img = cv2.line(img,(x, 0), (x, alto), color, grosor)
#for y in range(0,alto+1,cuadricula):
#    img = cv2.line(img,(0,y),(ancho,y),color,grosor)

#cv2.namedWindow("Cuadro",cv2.WINDOW_NORMAL)
#cv2.arrowedLine(img,(350,50),(450,100),color,4)
     #Colocar flecha a la cara de la niña 
#cv2.imshow("Cuadro",img)

#cv2.waitKey(0)
                         #Rectangulos
#import cv2
#img = cv2.imread("nina.jpg",1)
#color = (0,0,255)
#grosor = 1
#cara_x1,cara_x2 = 400,600
#cara_y1,cara_y2=40,250

#cv2.rectangle(img,(cara_x1,cara_y1),(cara_x2,cara_y2),color,grosor)
#cv2.imshow("Cuadro",img)
#cv2.waitKey(0)

                         #Circulos y elipses
#import cv2
#img = cv2.imread("nina.jpg",1)
#alto,ancho,_= img.shape
#color =(0,0,255)
#incremenrto_radio = 80
#grosor = 40

#centro_x = int(ancho/2)
#centro_y =int(alto/2)

#for radio in range(0,int(alto/2)+1, incremenrto_radio):
#     cv2.circle(img,(centro_x,centro_x),radio,color,grosor)

#cv2.imshow("Cuadro",img)
#cv2.waitKey(0)

                         #Textos
import cv2
img = cv2.imread("nina.jpg",1)
img_original = img.copy()

color = (0,0,255)
grosor = 4
fuente = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
escala = 2

#(ancho_texto,alto_texto),_ = cv2.getTextSize("Isabel",fuente,escala,grosor)
alto_imagen,ancho_imagen,_=img.shape

def actualizar_imaen(escala):
     img = img_original.copy()
     posicion_x,posicion_y = centrarImagen(escala)
     cv2.putText(img,"Isabel",(posicion_x,posicion_y),fuente,escala,color,grosor)
     cv2.imshow("Cuadro",img)

def centrarImagen(escala):
     (ancho_texto,alto_texto),_= cv2.getTextSize("Isabel",fuente,escala,grosor)
     posicion_x = int((ancho_imagen-ancho_texto)/2)
     posicion_y = int((alto_imagen-alto_texto)/2)
     
     return posicion_x,posicion_x

posicion_x, posicion_y = centrarImagen(escala)
cv2.putText(img,"Isabel",(posicion_x,posicion_y),fuente,escala,color,grosor)
cv2.imshow("Cuadro",img)
cv2.createTrackbar("Escala Texto","Cuadro",2,5,actualizar_imaen)

#posicion_x=int((ancho_imagen-ancho_texto)/2)
#posicion_y = int(alto_imagen/2 + alto_texto/2)


#cv2.arrowedLine(img,(200,100),(300,150),color,grosor)
#cv2.putText(img,"Isabel",(posicion_x,posicion_y),fuente,escala,color,grosor)



cv2.waitKey(0)