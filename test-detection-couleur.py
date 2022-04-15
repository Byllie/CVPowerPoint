import cv2
import math
from numpy import *

from time import *

def test () :
    video = cv2.VideoCapture(0)




    taille = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))

    tm = time()

    while time()-tm <= 5:
        ret, frame = video.read()

        coord=(taille[0]//2, taille[1]//2)
        cv2.circle(frame, coord, 3, (255, 0, 0), -1)
        cv2.imshow("bla", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

    video.release()
    cv2.destroyAllWindows()

    c=frame[coord[0]][coord[1]]
    print(c)
    video = cv2.VideoCapture(0)

    # Couleurs à détecter (bleu).
    d = array([int(c[0]*0.9), int(c[1]*0.9), int(c[2]*0.9)])
    f = array([int(c[0]*1.1), int(c[1]*1.1), int(c[2]*1.1)])
    print(d, f)

    while True :
        ret, frame = video.read()


        i = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #fenêtre de couleur daltoniennes
        #mask = cv2.inRange(i, d, f) # detection de couleur avec l'image aux couleurs chelous
        mask = cv2.inRange(frame, d, f)
        j = cv2.bitwise_and(frame, frame, mask=mask)

        x, y, largeur, longueur = cv2.boundingRect(mask)
        r, g, b = cv2.split(cv2.cvtColor(frame, cv2.COLOR_BGR2HSV))


        coord = (x + (largeur//2), y + (longueur//2))
        cv2.circle(frame, coord, 3, (0, 0, 255), -1)
        cv2.imshow("1", mask)
        cv2.imshow("2", frame)
        #cv2.imshow("3", j)


        print(frame[100][100])
        #cv2.imshow("5", r)
        #cv2.imshow("6", g)
        #cv2.imshow("7", b)
        cv2.imshow("4", i)




        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

    video.release()
    cv2.destroyAllWindows()

test()
