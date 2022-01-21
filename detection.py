import cv2
from time import *

from numpy import *


video = cv2.VideoCapture(0)
ret, frame = video.read()

f2 =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

while True :
    ret, frame = video.read()
    f1 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    f3 = list(f1)

    for i in range(len(f1)) :
        for y in range(len(f1[0])) :
            if f1[i][y] - f2[i][y] > 50 or f1[i][y] - f2[i][y] < -50 :
                pass
            else :
                f3[i][y] = 0

    cv2.imshow("", array(f3))

    f2 = array(f1)





    if cv2.waitKey(1) & 0xFF == ord('q') :
        break

video.release()
cv2.destroyAllWindows()

