import cv2

#Aplicación para leer una imagen desde dispositivo
#Declara variable asignar el contenido de una imagen mediante imread
imagen = cv2.imread('una.png')

#Mostrar en ventana el contenido de mi variable
cv2.imshow('ImagenUNA',imagen)

#Pausa Press any key
cv2.waitKey(0)
cv2.destroyAllWindows()

#Guardar una imagen procesada o leida en escala de gris
imagen = cv2.imread('una.png',0)
cv2.imshow('ImagenUNA',imagen)
#Pausa Press any key
cv2.waitKey(0)
cv2.imwrite('unaGris.jpg',imagen)
cv2.destroyAllWindows()