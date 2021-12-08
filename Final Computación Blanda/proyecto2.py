import numpy as np
import cv2
import os
from mate import operacion

ubicacion_frames = "C:/Users/hp/Desktop/Proyecto Video/frames" #cambiamos el xd por frames
file_names = os.listdir(ubicacion_frames)

imagenes = []
posicion_img= 0
img_iguales = 0
tiempo_img = []

# leo las imagenes de mi carpeta frames y las meto en un vector llamado imagenes
for n in file_names:
    imagen_path = ubicacion_frames+"/"+n
    img = cv2.imread(imagen_path,0)
    imagenes.append(img)

#visualizar las imagenes
    #cv2.imshow("Image",img)
    #cv2.waitKey(0)
#cv2.destroyAllWindows()

img1= cv2.imread('5000.png',0) # 0 para escala de grises , 1 para color

#leo la imagenes del arreglo imagenes
#luego uso substract para restar sus valores
# si son imagenes iguales entra al if

for imagen in imagenes:
    img2 = (imagen)
    diferencia = cv2.subtract(img1,img2)
    if not np.any(diferencia):
        img_iguales += 1 # aca guardamos cuantas imagenes repetidas hay
        op_minuto = ((posicion_img/30)/60)
        tiempo_exacto = operacion(op_minuto)
        tiempo_img.append(tiempo_exacto) # aca  guardamos el valor del tiempo que lleva

    posicion_img +=1



def informacion(vector,contador):
    for i in vector:
        minuto =  i
        print("la imagen se encuentra en el minuto: "+ str(minuto))
    if(contador == 0):
        print("no hay imagenes repetidas")
    else:
        print("la imagen se encuentra repetida :" + str(contador) +" veces")


informacion(tiempo_img,img_iguales)
