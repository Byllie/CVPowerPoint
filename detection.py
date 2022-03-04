import cv2
import  time
import math
from numpy import *
import tkinter
import ppt
import vecteur


def capture(Sensibilité,Pixelisation, sensibilite_vecteur):
    i = False

    time.sleep(5)
    back = cv2.createBackgroundSubtractorMOG2()
    video = cv2.VideoCapture(0)
    element = ones((Pixelisation, Pixelisation), uint8)
    back.setVarThreshold(Sensibilité)
    #variable pour vecteur
    temps_depuis_derniere_coord=0
    l_coord=[]
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

        if i is True :
            cv2.line(frame, l_coord[0], l_coord[1], (255, 0, 0), 2)
            cv2.line(frame, l_coord[1], l_coord[2], (255, 0, 0), 2)
            cv2.line(frame, l_coord[2], l_coord[3], (255, 0, 0), 2)

        cv2.imshow("Cam2",frame)
        cv2.imshow("Background", back.getBackgroundImage())
        cv2.imshow("Cam", masque)
        #Calcul des vecteurs
        if time.time()-temps_depuis_derniere_coord>0.25:
            if len(l_coord)==4:
                l_coord.pop(0)
                l_coord.append(gauche)
                v03 = vecteur.Vecteur(l_coord[0], l_coord[3])
                v01 = vecteur.Vecteur(l_coord[0], l_coord[1])
                v12 = vecteur.Vecteur(l_coord[1], l_coord[2])
                v23 = vecteur.Vecteur(l_coord[2], l_coord[3])
                print(v03.module,v03.argument)
                i = False
                if v03.module > sensibilite_vecteur :
                    print("module 3 ok")
                    if v03.argument>7*math.pi/4 or v03.argument<math.pi/4:
                        print("argument 3 ok")

                        if v01.module > v03.module*0.1 and v12.module > v03.module*0.1 and v23.module > v03.module*0.1 :
                            print("Module petits vecteurs OK")
                            if (v01.argument < math.pi / 2 or v01.argument > 3*math.pi / 2) and (v12.argument < math.pi / 2 or v12.argument > 3*math.pi / 2) and (v23.argument < math.pi / 2 or v23.argument > 3*math.pi / 2) :
                                print("Argument petits vecteurs OK")
                                i = True
                                ppt.mouvement("Bras-Gauche")
                temps_depuis_derniere_coord=time.time()


            else:
                l_coord.append(gauche)
                temps_depuis_derniere_coord=time.time()

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
slider3 = tkinter.Scale(Fenetre_tkinter, from_=10, to=500,orient='horizontal')
slider3.set(100)
slider1.pack()
slider2.pack()
slider3.pack()
bouton = tkinter.Button(Fenetre_tkinter,text="Lancer la camera",command=lambda:capture(slider2.get(),slider1.get(), slider3.get()))
bouton.pack()
Fenetre_tkinter.mainloop()
