from pickletools import uint8
import cv2
import numpy
#matriz = [[0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0]]
#img = numpy.array(matriz)
#print(img)

img = numpy.ones((500,500,3),numpy.uint8)*255

cv2.imshow("Matriz",img)









cv2.waitKey(0)

