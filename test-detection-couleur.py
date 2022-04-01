import cv2
import math
from numpy import *

def test () :
    video = cv2.VideoCapture(0)

    # Couleurs à détecter (bleu).
    d = array([95, 100, 50])
    f = array([105, 255, 255])

    while True :
        ret, frame = video.read()

        i = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(i, d, f)
        j = cv2.bitwise_and(frame, frame, mask=mask)

        x, y, largeur, longueur = cv2.boundingRect(mask)

        coord = (x + (largeur//2), y + (longueur//2))
        cv2.circle(frame, coord, 3, (0, 0, 255), -1)
        cv2.imshow("1", mask)
        cv2.imshow("2", frame)
        #cv2.imshow("3", j)
        #cv2.imshow("4", i)




        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

    video.release()
    cv2.destroyAllWindows()

test()
