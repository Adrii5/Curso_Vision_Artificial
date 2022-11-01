from heapq import merge
import cv2
img = cv2.imread('figuras geometricas.jpg',1)
img_azul, img_verde, img_roja = cv2.split(img)
cv2.imshow('Azul',img_azul)
cv2.imshow('Verde',img_verde)
cv2.imshow('roja',img_roja)
cv2.waitKey(0)
g = cv2.merge((img_azul,img_verde,img_roja))
cv2.imshow('Union',g)
cv2.waitKey(0)
