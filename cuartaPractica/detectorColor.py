import cv2
import numpy as np

#Este programa dectectara solo la precencia de un color usando HSV
#Hue, Saturation and Value
#Habilitamos la camara 
cap = cv2.VideoCapture(0)

#con un ciclo mostramos la ventana e interrumpimos hasta precionar la s
while True:
  ret,frame = cap.read()
  if ret==True:
    cv2.imshow('Camara de video', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
      break

#refrescamos la memoria
cap.release()
#cerramos ventana
cv2.destroyAllWindows()

#Proceso para comvertir una imagen de video a HSV
                    #H  S  V
redBajo1 = np.array([90,100,20], np.uint8)
redAlto1 = np.array([110,255,255], np.uint8)

redBajo2 = np.array([111,100,20], np.uint8)
redAlto2 = np.array([130,255,255], np.uint8)


cap = cv2.VideoCapture(0)

#con un ciclo mostramos la ventana e interrumpimos hasta precionar la s
while True:
  ret,frame = cap.read()
  if ret==True:
    #Conversion de un frame a un frameHSV
    frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    parametro1 = cv2.inRange(frameHSV,redBajo1,redAlto1)
    parametro2 = cv2.inRange(frameHSV,redBajo2,redAlto2)
    fusion = cv2.add(parametro1,parametro2)
    #Video original
    cv2.imshow('Video Original', frame)
    #Video ConvertidoHSV
    cv2.imshow('Video Fusion', fusion)

    if cv2.waitKey(1) & 0xFF == ord('s'):
      break

#refrescamos la memoria
cap.release()
#cerramos ventana
cv2.destroyAllWindows()