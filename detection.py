import cv2
import  time
import math
from numpy import *
import tkinter
import ppt
import vecteur
from tkinter import colorchooser


def capture(Sensibilité,Pixelisation, sensibilite_vecteur,mode):
        print(modedefonctionement.get())
        i = False
        time.sleep(5)
        back = cv2.createBackgroundSubtractorMOG2()
        video = cv2.VideoCapture(0)
        taille = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
        element = ones((Pixelisation, Pixelisation), uint8)
        back.setVarThreshold(Sensibilité)
        #variable pour vecteur
        temps_depuis_derniere_coord=0
        l_coord=[]
        if modedefonctionement.get()==0:
            mouvement=[vecteur.Deplacement((math.pi/4,7*math.pi/4),(math.pi/2,3*math.pi/2),1,ppt.droite),vecteur.Deplacement((5*math.pi/4,3*math.pi/4),(3*math.pi/2,math.pi/2),0,ppt.gauche)]
        else:
            mouvement=[vecteur.Deplacement((math.pi/4,7*math.pi/4),(math.pi/2,3*math.pi/2),1,ppt.suivant),vecteur.Deplacement((5*math.pi/4,3*math.pi/4),(3*math.pi/2,math.pi/2),0,ppt.precedent),vecteur.Deplacement((3*math.pi/4,math.pi/4),(math.pi,0),0,ppt.volumeplus),vecteur.Deplacement((7*math.pi/4,5*math.pi/4),(2*math.pi,math.pi),0,ppt.volumemoins)]
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

def ChoisirCouleurEcran () :
    video = cv2.VideoCapture(0)
    taille = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    tm = time.time()

    while time.time()-tm <= 5:
        ret, frame = video.read()
        frame = cv2.erode(frame, ones((10, 10), uint8), iterations=2)
        coord=(taille[0]//2, taille[1]//2)
        cv2.circle(frame, coord, 3, (255, 0, 0), -1)
        cv2.imshow("Couleur", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break
    video.release()
    cv2.destroyAllWindows()
    c=frame[coord[0]][coord[1]]
    c[0],c[2]=c[2],c[0]
    textecouleur.set(RgbVersHex(c))
def suiviMain(couleur):
    couleur=couleur[0][0]
    video = cv2.VideoCapture(0)
    haut = array([int(couleur[0] * 1.2), int(couleur[1] * 1.5), 255])
    bas = array([int(couleur[0] * 0.8), int(couleur[1] * 0.5), 50])
    while 1:
        a, image = video.read()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        masque = cv2.inRange(hsv, bas, haut)
        sortie = cv2.bitwise_and(image, image, mask=masque)
        cv2.imshow("Detection de couleur", sortie)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
#Fonction pour Tkinter. Les objet sont définis plus bas
def SourisTk():
    slider1.grid_remove()
    slider2.grid_remove()
    slider3.grid_remove()
    l1.grid_remove()
    l2.grid_remove()
    l3.grid_remove()
    boutonsouris.grid(row=1,column=0,sticky="n")
    labelsouris.grid(row=1,column=1)
    boutoncouleurecran.grid(row=4,column=1)
def PowerPointTk():
    boutoncouleurecran.grid_remove()
    labelsouris.grid_remove()
    boutonsouris.grid_remove()
    l1.grid(row=1,column=0,sticky='se')
    l3.grid(row=3,column=0,sticky='se')
    l2.grid(row=2,column=0,sticky='se')
    slider1.grid(row = 1, column = 1,columnspan=2)
    slider2.grid(row = 2, column = 1,columnspan=2)
    slider3.grid(row = 3, column = 1,columnspan=2)

def ChoisirCouleur():
    couleur=tkinter.colorchooser.askcolor(color=None,title ="Choisir une Couleur")
    textecouleur.set(couleur[1])

def CouleurOK(couleurhex):
    couleurhex=couleurhex[1::]
    couleurhex=couleurhex.upper()
    i=True
    if len(couleurhex)==6:
        for y in couleurhex:
            if y not in ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F"]:
                i=False
    else:
        i=False
    return "#"+couleurhex if i else "#FFF"

def RgbVersHex(rgb):
    hexa='#'
    for i in rgb:
        hexa=hexa+hex(i)[2::] if i>15 else hexa+"0"+hex(i)[2::]
    return hexa.upper()

#Tkinter
Fenetre_tkinter=tkinter.Tk()
Fenetre_tkinter.iconbitmap('main-rouge.ico')
img = tkinter.PhotoImage(file="logo-magic-hand.png")
label = tkinter.Label(Fenetre_tkinter, image = img)
Fenetre_tkinter.geometry("520x400")
Fenetre_tkinter.title("MagicHand")
tkinter.Frame(Fenetre_tkinter).grid()
modedefonctionement=tkinter.IntVar()
modedefonctionement.set=0
textecouleur=tkinter.StringVar()
textecouleur.set("#FFFFFF")
slider1 = tkinter.Scale(Fenetre_tkinter, from_=0, to=25,orient='horizontal',length=350,width=10)
slider1.set(4)
slider2 = tkinter.Scale(Fenetre_tkinter, from_=0, to=500,orient='horizontal',length=350,width=10)
slider2.set(100)
slider3 = tkinter.Scale(Fenetre_tkinter, from_=0, to=50,orient='horizontal',length=350,width=10)
slider3.set(10)
radio1=tkinter.Radiobutton(Fenetre_tkinter,text="PowerPoint",variable=modedefonctionement,value=0,command=PowerPointTk)
radio2=tkinter.Radiobutton(Fenetre_tkinter,text="Musique",variable=modedefonctionement,value=1,command=PowerPointTk)
radio3=tkinter.Radiobutton(Fenetre_tkinter,text="Souris",variable=modedefonctionement,value=2,command=SourisTk)
l1=tkinter.Label(Fenetre_tkinter,text="Pixelisation : ")
l2=tkinter.Label(Fenetre_tkinter,text="Sensibilité : ")
l3=tkinter.Label(Fenetre_tkinter,text="% pour mouvement :")
bouton = tkinter.Button(Fenetre_tkinter,text="Lancer la camera",command=lambda:capture(slider2.get(),slider1.get(), slider3.get(),modedefonctionement) if modedefonctionement.get()!=2 else suiviMain(cv2.cvtColor (uint8([[[int(textecouleur.get()[5:],16),int(textecouleur.get()[3:5],16),int(textecouleur.get()[1:3],16)]]]),cv2.COLOR_BGR2HSV)),width  =50)
boutonsouris=tkinter.Button(Fenetre_tkinter,text="Choisir une couleur",command=ChoisirCouleur)
labelsouris=tkinter.Entry(Fenetre_tkinter,textvariable=textecouleur)
textecouleur.trace_add("write",lambda *args: labelsouris.config(bg=CouleurOK(textecouleur.get())))
bouton.grid(row=6,column=0,columnspan=3)
boutoncouleurecran= tkinter.Button(Fenetre_tkinter,text="Choisir la couleur depuis la caméra",command=ChoisirCouleurEcran)
label.grid(row=0,column=0,columnspan=3)
radio1.grid(row=5,column=0)
radio2.grid(row=5,column=1)
radio3.grid(row=5,column=2)

PowerPointTk()
Fenetre_tkinter.mainloop()
