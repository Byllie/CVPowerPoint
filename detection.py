import cv2
import  time
from numpy import *
import tkinter
import ppt
def capture(Sensibilité,Pixelisation):

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
        cv2.imshow("Cam2",frame)
        cv2.imshow("Background", back.getBackgroundImage())
        cv2.imshow("Cam", masque)
        #Calcul des vecteurs
        if time.time()-temps_depuis_derniere_coord>0.25:
            if len(l_coord)==4:
                l_coord.pop(0)
                l_coord.append(gauche)
                v3=(l_coord[3][0]-l_coord[0][0],l_coord[3][1]-l_coord[0][1])
                #print(v3)
                if v3[0]>50 and -20<v3[1] and 20>v3[1]:
                    print("bob")
                    ppt.mouvement("Bras-Gauche")
                temps_depuis_derniere_coord=time.time()

                calc_vecteur(l_coord)
            else:
                l_coord.append(gauche)
                temps_depuis_derniere_coord=time.time()


        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
    video.release()
    cv2.destroyAllWindows()


def calc_vecteur (c) :
    v1=(c[1][0]-c[0][0],c[1][1]-c[0][1])
    v2=(c[2][0]-c[1][0],c[2][1]-c[1][1])
    v3=(c[3][0]-c[2][0],c[3][1]-c[2][1])

    if v1[0]>50 and -20<v3[1] and 20>v3[1] :
        print(v1, v2, v3)

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
