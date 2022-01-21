import cv2
from time import *

from numpy import *


def capture():
    back = cv2.createBackgroundSubtractorMOG2()
    video = cv2.VideoCapture(0)
    element = ones((4, 4), uint8)
    back.setVarThreshold(100)
    while True :
        ret, frame = video.read()
        masque = back.apply(frame,None,0)
        masque = cv2.erode(masque, element, iterations=1)
        cv2.imshow("Cam", masque)




        if cv2.waitKey(1) & 0xFF == ord('q') :
            break

    video.release()
    cv2.destroyAllWindows()
import  time
time.sleep(5)
capture()