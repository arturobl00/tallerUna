import cv2
#Declaramos una variable y le asignamos el valor de VideoCapture
#Esta funcion inicia la camara del dispositivo
captura = cv2.VideoCapture(0)
#Guardar el video manejamos 4 propiedades o parametros
#Nombre y ext
#Codificador de video
#Fotogramas x Seg FPS
#Tamaño
salida = cv2.VideoWriter('miVideo.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(640,480))

#Crear ciclo para el gravado de video
while(captura.isOpened()):
    #Decalramos 2 parametros
    ret, imagen = captura.read()
    #Mostrar el video en una ventana
    if ret == True:
        cv2.imshow('Camara Activa',imagen)
        salida.write(imagen)
        #Condicion para detener la capatura
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

captura.release()
salida.release()
cv2.destroyAllWindows()

#Asignar el video grabado a captura
captura = cv2.VideoCapture('miVideo.avi')

#Crear ciclo para mostrar el video capturado
while(captura.isOpened()):
    #Decalramos 2 parametros
    ret, imagen = captura.read()
    #Mostrar el video en una ventana
    if ret == True:
        #Reproductor
        cv2.imshow('Video Reproduciendo',imagen)
        if cv2.waitKey(40) & 0xFF == ord('s'):
            break
    else: break

captura.release()
cv2.destroyAllWindows()