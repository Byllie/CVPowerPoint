import cv2
import math
import numpy as np

def test () :
    video = cv2.VideoCapture(0)
    d = np.array([95, 100, 50])
    f = np.array([105, 255, 255])
    d = np.array([50, 95, 100])
    f = np.array([255, 105, 255])
    d = np.array([100, 50, 95])
    f = np.array([255, 255, 105])
    while True :
        ret, frame = video.read()

        i = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(i, d, f)
        j = cv2.bitwise_and(frame, frame, mask=mask)

        x, y, largeur, longueur = cv2.boundingRect(mask)

        coord = (x + (largeur//2), y + (longueur//2))

        print(coord)
        cv2.imshow("1", mask)
        cv2.imshow("2", frame)
        #cv2.imshow("3", j)
        #cv2.imsqhow("4", i)




        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
    print(frame)
    video.release()
    cv2.destroyAllWindows()

test()
