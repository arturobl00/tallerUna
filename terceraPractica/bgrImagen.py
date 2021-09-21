#Importamos librerias numpy incluye funciones para proceso de imagenes
from typing import ByteString
import cv2
import numpy as np

#Mostrar imagen original
imgOriginal = cv2.imread('chica.jpg')
cv2.imshow('Chica Original',imgOriginal)

#Matriz de datos de la imagen
bgr = np.zeros((300,300,3),dtype=np.uint8)
bgr[:,:,:]=(255,255,255)
cv2.imshow('BGR Estatus',bgr)

#Asignar la imagen a bgr
bgr = cv2.imread('chica.jpg')
#Asignar escalas
e1 = bgr[:,:,0]
e2 = bgr[:,:,1]
e3 = bgr[:,:,2]

#Stack o congunto de imagenes
cv2.imshow('STack en BGR',np.hstack([e1,e2,e3]))

cv2.waitKey(0)
cv2.destroyAllWindows()