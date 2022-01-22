import cv2
import  time
from numpy import *
import tkinter


def capture(Sensibilité,Pixelisation):
    time.sleep(5)
    back = cv2.createBackgroundSubtractorMOG2()
    video = cv2.VideoCapture(0)
    element = ones((Pixelisation, Pixelisation), uint8)
    back.setVarThreshold(Sensibilité)
    while True :
        ret, frame = video.read()
        masque = back.apply(frame,None,0)
        masque = cv2.erode(masque, element, iterations=1)
        x, y, largeur, longueur = cv2.boundingRect(masque)
        cv2.rectangle(frame,(x,y),(x+largeur,y+longueur),(0,255,0),2)
        gauche = (x, argmax(masque[:, x]))
        droite = (x + largeur - 1, argmax(masque[:, x + largeur - 1]))
        haut = (argmax(masque[y, :]), y)
        bas = (argmax(masque[y + longueur - 1, :]), y + longueur - 1)
        cv2.circle(frame, gauche, 8, (255, 50, 0), -1)
        cv2.circle(frame, droite, 8, (255, 50, 0), -1)
        cv2.circle(frame, haut, 8, (255, 50, 0), -1)
        cv2.circle(frame, bas, 8, (255, 50, 0), -1)
        cv2.imshow("Cam2",frame)
        cv2.imshow("Background", back.getBackgroundImage())
        cv2.imshow("Cam", masque)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
    video.release()
    cv2.destroyAllWindows()


#Tkinter
Fenetre_tkinter=tkinter.Tk()
tkinter.Frame(Fenetre_tkinter).pack()
slider1 = tkinter.Scale(Fenetre_tkinter, from_=0, to=25,orient='horizontal')
slider1.set(4)
slider2 = tkinter.Scale(Fenetre_tkinter, from_=0, to=500,orient='horizontal')
slider2.set(100)
slider1.pack()
slider2.pack()
bouton = tkinter.Button(Fenetre_tkinter,text="Lancer la camera",command=lambda:capture(slider2.get(),slider1.get()))
bouton.pack()
Fenetre_tkinter.mainloop()