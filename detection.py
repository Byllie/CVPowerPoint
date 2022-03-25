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
    taille = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    print(str(taille[0]) + "x" + str(taille[1]))
    element = ones((Pixelisation, Pixelisation), uint8)
    back.setVarThreshold(Sensibilité)
    #variable pour vecteur
    temps_depuis_derniere_coord=0
    l_coord=[]
    mouvement=[vecteur.Deplacement((math.pi/4,7*math.pi/4),(math.pi/2,3*math.pi/2),1,ppt.droite),vecteur.Deplacement((5*math.pi/4,3*math.pi/4),(3*math.pi/2,math.pi/2),0,ppt.gauche)]
    while True:
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
                if v03.module > math.sqrt(taille[0]**2 + taille[1]**2) * sensibilite_vecteur / 100 :
                        if v01.module > v03.module*0.1 and v12.module > v03.module*0.1 and v23.module > v03.module*0.1 :
                            for mv in mouvement:
                                if {1:v03.argument<mv.a1[0] or v03.argument>mv.a1[1], 0:v03.argument<mv.a1[0] and v03.argument>mv.a1[1]}[mv.andor]:
                                    if {1:(v01.argument < mv.a2[0] or v01.argument > mv.a2[1]) and (v12.argument < mv.a2[0] or v12.argument > mv.a2[1]) and (v23.argument < mv.a2[0] or v23.argument > mv.a2[1]), 0:(v01.argument < mv.a2[0] and v01.argument > mv.a2[1]) and (v12.argument < mv.a2[0] and v12.argument > mv.a2[1]) and (v23.argument < mv.a2[0] and v23.argument > mv.a2[1])}[mv.andor]:
                                        i=True
                                        mv.f()
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
Fenetre_tkinter.iconbitmap('main-rouge.ico')
img = tkinter.PhotoImage(file="logo-magic-hand.png")
label = tkinter.Label(Fenetre_tkinter, image = img)
# label.pack()
Fenetre_tkinter.geometry("520x380")
Fenetre_tkinter.title("MagicHand")
tkinter.Frame(Fenetre_tkinter).grid()
slider1 = tkinter.Scale(Fenetre_tkinter, from_=0, to=25,orient='horizontal',length=350,width=10)
slider1.set(4)
slider2 = tkinter.Scale(Fenetre_tkinter, from_=0, to=500,orient='horizontal',length=350,width=10)
slider2.set(100)
slider3 = tkinter.Scale(Fenetre_tkinter, from_=0, to=50,orient='horizontal',length=350,width=10)
slider3.set(10)
slider1.grid(row = 1, column = 1)
slider2.grid(row = 2, column = 1)
slider3.grid(row = 3, column = 1)
label.grid(row=0,columnspan=2)
tkinter.Label(Fenetre_tkinter,text="Pixelisation : ").grid(row=1,column=0,sticky='se')
tkinter.Label(Fenetre_tkinter,text="Sensibilité : ").grid(row=2,column=0,sticky='se')
tkinter.Label(Fenetre_tkinter,text="% pour mouvement :").grid(row=3,column=0,sticky='se')
bouton = tkinter.Button(Fenetre_tkinter,text="Lancer la camera",command=lambda:capture(slider2.get(),slider1.get(), slider3.get()),width  =50)
bouton.grid(row=4,column=0,columnspan=2)
Fenetre_tkinter.mainloop()
