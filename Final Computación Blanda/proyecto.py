import cv2

capture = cv2.VideoCapture('perros y gatos 2.mp4')
ubicacion_frames = (r'C:\Users\hp\Desktop\Proyecto Video\frames/')
contador = 0

while (capture.isOpened()):
    ret, frame = capture.read()
    if(ret == True):
        cv2.imwrite(ubicacion_frames + 'IMG_%04d.png' % contador, frame)
        contador +=1
        if(cv2.waitKey(1) == ord('s')):
            break
    else:
        break

capture.release() # liberamos la captura
cv2.destroyAllWindows() # destruimos todas las ventanas que se pudieron generar
