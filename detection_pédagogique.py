import cv2
from time import *

from numpy import *


def background():
    algo_effacer_background= cv2.createBackgroundSubtractorMOG2()
    return algo_effacer_background

def capture(back,b2):
    video = cv2.VideoCapture(0)
    element = ones((4, 4), uint8)
    back.setVarThreshold(100)
    while True :
        ret, frame = video.read()
        masque_pure = b2.apply(frame, None, 0)
        masque = back.apply(frame,None,0)
        masque2 = cv2.erode(masque, element, iterations=1)
        img=back.getBackgroundImage()
        cv2.imshow("Threshold+erode", masque2)
        cv2.imshow("Threshold", masque)
        cv2.imshow("Algo-pure", masque_pure)
        cv2.imshow("Video direct", frame)
        cv2.imshow("Background", img)




        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

    video.release()
    cv2.destroyAllWindows()

import time
a=background()
b=background()
time.sleep(5)
capture(a,b)