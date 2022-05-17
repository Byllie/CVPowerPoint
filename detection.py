import cv2
import  time
import math
from numpy import *
import tkinter
from tkinter import colorchooser
#import de ppt.py et vecteur.py
import ppt
import vecteur


def capture(Sensibilité,Pixelisation, sensibilite_vecteur,mode):
        """
        Fonction gérant tout la détection de mouvement, l'affichage des fenêtre vidéos et des visuels ajoutés (rectangles, points, etc...) et déclanchant les différentes actions.
        """
        i = False#i est une variable bouléenne qui suit si le mouvement est corect
        time.sleep(5)#5 sec pour avoir le temps de partir afin de prendre une photo du fond
        back = cv2.createBackgroundSubtractorMOG2() #algorythme permettant de suprimer le fond
        video = cv2.VideoCapture(0) #permet de lancer une capture vidéo, 0 corespond à l'id de la caméra 0 : la première caméra du pc. Dans le cas où l'on veut changer de caméra il faut changer le 0 par l'id de la caméra-
        taille = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))) #on récupére les dimensions en px de la camera dans un tuple
        element = ones((Pixelisation, Pixelisation), uint8) #creer une liste Pixelisation*pixelisation avec numpy (5*5 par exemple), uint8 désigne un entier sur 8 bit 2^8=255 pour le rgb
        back.setVarThreshold(Sensibilité) #on modifie le treshold de l'algo de supression de fond, plus la valeur est haute et plus l'algorithme considère des pixels éloignés (en couleur) comme faisant partie du background
        #variable pour vecteur
        temps_depuis_derniere_coord=0#variable qui a le time où les derniers vecteurs ont été calculés
        l_coord=[]#liste des positions sucessives de la main
        if modedefonctionement.get()==0:#mode0 ==mode powerpoint , mode1==mode musique
            #définition des mouvements à l'aide de la Class Deplaccement de vecteur.py pour powerpoint
            mouvement=[vecteur.Deplacement((math.pi/4,7*math.pi/4),(math.pi/2,3*math.pi/2),1,ppt.droite),vecteur.Deplacement((5*math.pi/4,3*math.pi/4),(3*math.pi/2,math.pi/2),0,ppt.gauche)]
        else:
            #mouvement pour la musique
            mouvement=[vecteur.Deplacement((math.pi/4,7*math.pi/4),(math.pi/2,3*math.pi/2),1,ppt.droite),vecteur.Deplacement((5*math.pi/4,3*math.pi/4),(3*math.pi/2,math.pi/2),0,ppt.gauche),vecteur.Deplacement((3*math.pi/4,math.pi/4),(math.pi,0),0,ppt.volumemoins),vecteur.Deplacement((7*math.pi/4,5*math.pi/4),(2*math.pi,math.pi),0,ppt.volumeplus)]
        while True:
            ret, frame = video.read()# on récupère l'image de la caméra: frame est une liste de liste de tuple (b,g,r (c'est du rgb mais pas dans le même sens parce que open cv voulait se sentir diffèrent) d'entiers codés sur 8 bit(255)
            masque = back.apply(frame,None,0)#on applique l'algorythme de substraction de l'arrière plan, cela renvoit un masque (0 ou 1) pour chaque pixel, un 1 montre un pixel qui a changé signicativement par rapport au fond
            masque = cv2.erode(masque, element, iterations=1)#on applique un effet d'érosion sur le masque, on prend des carrées de élement(15*15 par exemple) sur l'image et on calcule une moyenne locale puis on définit la valeur de chaque pixel du carrée à la moyenne des valeurs arondies à l'entier le plus prés, cela permet de se débarrasser des pixels de bruit qui parasitent l'écran
            x, y, largeur, longueur = cv2.boundingRect(masque)#on utilise la fonction bouding rect qui renvoie les coordonnées x,y du coin supérieur ainsi que la largeur et la longueur du plus petit rectangle contenant tous les pixels de valeur 1, on obtient un rectangle qui fait le "contour" des pixels qui ne font pas partie du fond
            cv2.rectangle(frame,(x,y),(x+largeur,y+longueur),(0,255,0),2)#on afiche un rectangle sur le retour caméra avec les coordonnées precedents. Malheuresement open CV n'est JAMAIS consistant donc ici il faut donner les coordonnées du point supérieur gauche et inférieur droit alors que la fonction boundringrec renvoie un rectangle avec sa largeur et sa longueur, Bref trop de souffrance
            gauche = (x, argmax(masque[:, x])) #alors en fait on sait que sur l'axe x=x il y a le pixel le plus à gauche qui a des coordonnées de la forme (x,?), pour ? on va prendre le premier 1 de la  colone. On a ainsi les coordonnées du pixel le plus à gauche de la main
            droite = (x + largeur - 1, argmax(masque[:, x + largeur - 1])) #pareil pour le pixel le plus à droite (le -1 est la car x+largeur donne une valeur avec 1 de trop pour les cordonnés x de la droite de droite)
            haut = (argmax(masque[y, :]), y)#pareil
            bas = (argmax(masque[y + longueur - 1, :]), y + longueur - 1)#extrement similaire
            cv2.circle(frame, gauche, 8, (255, 50, 0), -1) #on place un point sur lécran au coordonnée du pixel le plus à gauche. (255,50,0) désigne la couleur (en rgb ici pas en bgr parce que pourquoi pas) -1 est la largeur des bord du cercle,-1 permet de remplir le cercle afin d'avoir un point
            cv2.circle(frame, droite, 8, (255, 50, 0), -1)#idem pour le point le plus à droite
            cv2.circle(frame, haut, 8, (255, 50, 0), -1)#idem
            cv2.circle(frame, bas, 8, (255, 50, 0), -1)#pareil

            if i is True :#si le mouvement est corecte, on affiche les "vecteurs", en reliant les coordonnées successives de la main stockées dans lcord
                cv2.line(frame, l_coord[0], l_coord[1], (255, 0, 0), 2)
                cv2.line(frame, l_coord[1], l_coord[2], (255, 0, 0), 2)
                cv2.line(frame, l_coord[2], l_coord[3], (255, 0, 0), 2)

            cv2.imshow("Cam2",frame)#on affiche le retour caméra + les lignes +les rectangles +les points calculés precedement
            cv2.imshow("Background", back.getBackgroundImage())#on affiche le background considéré par l'algorythme
            cv2.imshow("Cam", masque)#on renvoie le masque obtenu
            #Calcul des vecteurs
            if time.time()-temps_depuis_derniere_coord>0.25:#on calcule les vecteurs tous les 0.25 sec
                if len(l_coord)==4:#si il y a 4 coord dans l_coord
                    l_coord.pop(0)#on enlève le 4 ème point (le position de la main la plus vieille)
                    l_coord.append(gauche)#on rajoute en 4ème position de la liste la position de la main gauche
                    v03 = vecteur.Vecteur(l_coord[0], l_coord[3])#vecteur de deplacement total de 0 à 3
                    v01 = vecteur.Vecteur(l_coord[0], l_coord[1])#vecteur de 0 à 1
                    v12 = vecteur.Vecteur(l_coord[1], l_coord[2])#vecteur de 1 à 2
                    v23 = vecteur.Vecteur(l_coord[2], l_coord[3])#vecteur de 2 à 3
                    i = False #pour l'instant les vecteurs ne sont pas "valides"
                    if v03.module > math.sqrt(taille[0]**2 + taille[1]**2) * sensibilite_vecteur / 100 :#premier test : est ce que le vecteur est assez grand par rapport à un  % de  la diagonale de l'écran
                            if v01.module > v03.module*0.1 and v12.module > v03.module*0.1 and v23.module > v03.module*0.1 : #est ce que les vecteurs intermédiaires ne sont pas trop petits (mouvement brutal) ou fausse détection
                                for mv in mouvement:#pour chaque type de mouvement du mode
                                    if {1:v03.argument<mv.a1[0] or v03.argument>mv.a1[1], 0:v03.argument<mv.a1[0] and v03.argument>mv.a1[1]}[mv.andor]:#on vérifie que le grand vecteur a un argument dans l'angle du mouvement par exemple entre pi/4 et 3pi/4 pour un mouvement par le haut
                                        if {1:(v01.argument < mv.a2[0] or v01.argument > mv.a2[1]) and (v12.argument < mv.a2[0] or v12.argument > mv.a2[1]) and (v23.argument < mv.a2[0] or v23.argument > mv.a2[1]), 0:(v01.argument < mv.a2[0] and v01.argument > mv.a2[1]) and (v12.argument < mv.a2[0] and v12.argument > mv.a2[1]) and (v23.argument < mv.a2[0] and v23.argument > mv.a2[1])}[mv.andor]:#les vecteur intermèdiaire ont argument qui va globalement dans la bonne direction (dans la bonne moitiè du cercle trigo)
                                            i=True#on met i sur true pour afficher les vecteurs pendant 0.25sec jusqu'au prochain calcul
                                            mv.f()#on execute la fonction liée au mouvement, un mouvement vers la gauche en powerpoint va lancer ptt.gauche()
                    temps_depuis_derniere_coord=time.time()#on reset le timer


                else:#si il y a moins de 4 coordonées dans la liste == début de programmes (moins de 1 sec depuis le lancement)
                    l_coord.append(gauche)#on rajoute les coordonnées et reset le timer,on enlève rien de liste car elle n'a pas plus que 4 points
                    temps_depuis_derniere_coord=time.time()

            if cv2.waitKey(1) & 0xFF == ord('q') :#si la touche q du clavier est appuyée
                break#on sort de while
        video.release()#on arrète le capture vidéo
        cv2.destroyAllWindows() #et on ferme toutes les fenètres

def ChoisirCouleurEcran () :
    """
    Fonction permettant de capturer la couleur placé au centre de l'image (sur la croix) et qui renvoie le code hexadécimal correspondant.
    """
    video = cv2.VideoCapture(0)
    taille = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))#similaire à Capture()
    tm = time.time()
    while time.time()-tm <= 5:#tant que moins de 5 sec sont passèes
        ret, frame = video.read()#on récupère l'image
        frame = cv2.erode(frame, ones((5, 5), uint8), iterations=1)#on érode l'image pour perdre les détails et rendre la selection de couleur plus simple (sinon on risque de selectionner des pixels de bruit, noir ou blanc), faire la moyenne locale des pixels permet de lisser l'image et les couleurs rendant moins fastidieux la recherche de pixels
        coord=(taille[1]//2, taille[0]//2)# les coordonnées du point au centre de l'écran
        cv2.circle(frame, coord, 8, tuple([int(i) for i in frame[coord[0]][coord[1]] ]), -1)# on affiche un cercle de la couleur du pixel du centre de l'écran, cercle de 8px comme ça on voit la couleur
        cv2.imshow("Couleur", frame)#on affiche l'image caméra
        if cv2.waitKey(1) & 0xFF == ord('q') :# si on appuyue sur q
            break
    video.release()#on libére la caméra
    cv2.destroyAllWindows()#Et on ferme les fenetres open cv
    c=frame[coord[0]][coord[1]]#on récupère la couleur du pixel du milieu
    c[0],c[2]=c[2],c[0]#on passe de bgr à rgb car Open CV a décidé de fonctionner en bgr pour aucune raison
    textecouleur.set(RgbVersHex(c))#on set le texte à la valeur hex de la couleur

def suiviMain(couleur):
    """
    Fonction gérant le suivi de la couleur précédemment sélectionnée, et les actions en découlant.
    """

    couleur=couleur[0][0]#on récupère la couleur qui était stockée dans une image Open Cv d'un pixel, on récupère donc le pixel de coordonnées 0,0 de l'image à un pixel
    #la couleur est en HSV https://fr.wikipedia.org/wiki/Teinte_Saturation_Valeur
    #HSV pemet de définir un panel de couleur facilement car contrairement au rgb, la couleur est contenue seulement dans H, la saturation dans S et le "contraste" dans V
    #ainsi pour que 2 couleurs soit ""proches" il faut seulement que le H soit extrement similaire, la saturation des deux coueleurs doit être "proche" et il suffit que le V ne soit pas trop bas (car sinon c'est juste du noir)
    #le HSV de Open est diffèrent du normal, il garde les informations dans des pixels "valides" en rgb dans H,S,V sont des entiers codés sur 8 bit(255) alors que le HSV clasique est en %
    video = cv2.VideoCapture(0)#on récupère la vidéo
    haut = array([int(couleur[0] * 1.2), int(couleur[1] * 1.5), 255])#on définit un couleur haute
    bas = array([int(couleur[0] * 0.8), int(couleur[1] * 0.5), 50])#et basse à partir de la couelur
    taille = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))#on récupère la taille
    while 1:
        a, image = video.read()#on récupère l'image
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)#on passe de BGR(rgb d'Open CV) aux HSV: https://fr.wikipedia.org/wiki/Teinte_Saturation_Valeur
        masque = cv2.inRange(hsv, bas, haut)#on crée un masque, les pixels qui sont dans le range couleur basse/haute sont "valides"==1 et les autres ==0
        masque = cv2.erode(masque, ones((50, 50), uint8), iterations=1)#On érode l'image pour enlever des détails (des pixels seuls de la bonne couleur,: des défauts de la caméra, une mouche qui vole...)
        sortie = cv2.bitwise_and(image, image, mask=masque)#on fait un and bit à bit entre le masque et l'image , les pixels 1 du masque vont être les pixels affichès


        x, y, largeur, longueur = cv2.boundingRect(masque)#j'ai juste  littèralement repris le rectangle Capture()
        cv2.rectangle(sortie, (x, y), (x + largeur, y + longueur), (0, 255, 0), 2)#pareil je l'ai déja expliqué plus haut
        cv2.circle(sortie,(x+largeur//2,y+longueur//2),6,(255,0,0),-1)#on affiche un point au centre du rectangle à la croisée des diagonales
        cv2.imshow("Detection de couleur", sortie)#on affiche l'image
        ppt.souris(x+largeur//2,y+longueur//2,taille)#on envoie les coordonnés x et y de la souris à ptt.souris()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()#si la touche q est appuyée, on ferme open cv
    cv2.destroyAllWindows()

def CouleurOK(couleurhex):
    """
    Fonction qui vérifie que le code hexadécimal rentré dans le champs de la fenêtre tkinter est bien valide, et si oui qui affiche (en arrière plan de ce champs) la couleur définie.
    """
    couleurhex=couleurhex[1::]
    couleurhex=couleurhex.upper()
    i=True
    if len(couleurhex)==6:
        for y in couleurhex:
            if y not in ["1","2","3","4","5","6","7","8","9","0","A","B","C","D","E","F"]:
                i=False
    else:
        i=False
    return "#"+couleurhex if i else "#FFFFFF" #on renvoie le hex s'il est valide sinon on renvoie #FFFFFFF :du blanc

def RgbVersHex(rgb):
    """
    Fonction qui prend en paramètre un tuple des trois codes RGB d'une couleur, et qui renvoie le code hexadécimal correpondant.
    """
    hexa='#'
    for i in rgb:
        hexa=hexa+hex(i)[2::] if i>15 else hexa+"0"+hex(i)[2::]
    return hexa.upper()

###################################
#Note: je ne vais pas commenter tous le Tkinter, c'est long et plutot simple je vais simplement commenter les choses intérréssantes
##################################


#Fonction pour Tkinter. Les objets sont définis plus bas
def SourisTk():
    """
    Fonction permettant à l'interface Tkinter de selectionner le mode "Souris" et ainsi de pouvoir bouger le curseur en fonction d'une certaine couleur.
    """
    #on enlève les élements du mode powerpoint et musique pour afficher les elements du mode souris
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
    """
    Fonction permettant à l'interface Tkinter de selectionner le mode "PowerPoint" et ainsi de pouvoir changer de slide tout en bougeant le bras droit.
    """
    #on enlève les élements du mode souris pour afficher ceux du mode musique et PowerPoint
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
    """
    Fonction qui ouvre la fenêtre de sélection de couleur et la renvoie dans Tkinter.
    """
    couleur=tkinter.colorchooser.askcolor(color=None,title ="Choisir une Couleur")
    textecouleur.set(couleur[1])#On met le texte à la couleur choisie


#Définition des objets Tkinter ils sont souvent affichés plus haut
#Tkinter
Fenetre_tkinter=tkinter.Tk()#fenetre principale
Fenetre_tkinter.iconbitmap('main-rouge.ico')#icone en haut de la fenetre
img = tkinter.PhotoImage(file="logo-magic-hand.png")#On load le logo
label = tkinter.Label(Fenetre_tkinter, image = img)#On met l'image dans un label
Fenetre_tkinter.geometry("520x400")#On définit les dimensions de la fenètre
Fenetre_tkinter.title("MagicHand")#On définit le nom de la fenêtre
tkinter.Frame(Fenetre_tkinter).grid()#On met le mode d'affichage à grid permettant de placer les elements dans une grille
modedefonctionement=tkinter.IntVar()#Les Int var sont des variables dynamiques si leur contenue change alors les affichages qui dépandent de la variable vont changer ex:si je définis un texte avec une variable et que je change la variable, le texte ne va pas changer . Avec un INTvar le texte change
modedefonctionement.set=0#on initialise avec un setter modedefonctionement à 0 (powerpoint)
textecouleur=tkinter.StringVar()#On crée un STRVar (meme principe que INTvar plus haut) qui va afficher le hex de la couleur
textecouleur.set("#FFFFFF")#On l'inialise en blanc
#slider du mode PowerPoint et Musique
slider1 = tkinter.Scale(Fenetre_tkinter, from_=0, to=25,orient='horizontal',length=350,width=10)
slider1.set(4)
slider2 = tkinter.Scale(Fenetre_tkinter, from_=0, to=500,orient='horizontal',length=350,width=10)
slider2.set(100)
slider3 = tkinter.Scale(Fenetre_tkinter, from_=0, to=50,orient='horizontal',length=350,width=10)
slider3.set(10)
#Les radios boutons pour changer de mode , ils font changer la variable mode de fonctionement et apeller les fonctions qui permettent d'afficher et de faire disparaite les élements concernés
radio1=tkinter.Radiobutton(Fenetre_tkinter,text="PowerPoint",variable=modedefonctionement,value=0,command=PowerPointTk)
radio2=tkinter.Radiobutton(Fenetre_tkinter,text="Musique",variable=modedefonctionement,value=1,command=PowerPointTk)
radio3=tkinter.Radiobutton(Fenetre_tkinter,text="Souris",variable=modedefonctionement,value=2,command=SourisTk)
#Le texte pour les sliders
l1=tkinter.Label(Fenetre_tkinter,text="Pixelisation : ")
l2=tkinter.Label(Fenetre_tkinter,text="Sensibilité : ")
l3=tkinter.Label(Fenetre_tkinter,text="% pour mouvement :")
#Bouton pour lancer le programme qui récupère les valeurs des sliders ou la couleur selon le mode. La fonction lambda est un peu longue mais avec du courage...
bouton = tkinter.Button(Fenetre_tkinter,text="Lancer la camera",command=lambda:capture(slider2.get(),slider1.get(), slider3.get(),modedefonctionement) if modedefonctionement.get()!=2 else suiviMain(cv2.cvtColor (uint8([[[int(textecouleur.get()[5:],16),int(textecouleur.get()[3:5],16),int(textecouleur.get()[1:3],16)]]]),cv2.COLOR_BGR2HSV)),width  =50)
boutonsouris=tkinter.Button(Fenetre_tkinter,text="Choisir une couleur",command=ChoisirCouleur)#Bouton qui lance la sélection de couleur depuis la fenêtre native
labelsouris=tkinter.Entry(Fenetre_tkinter,textvariable=textecouleur)#Le label souris où il est écrit la couleur
textecouleur.trace_add("write",lambda *args: labelsouris.config(bg=CouleurOK(textecouleur.get())))#Quand le texte est modifié, on change la couleur du background, on passe le texte  de CouleurOK pour empécher les erreurs quand on commence à taper une couleur ainsi #56 n'est pas un hex valide, la fonction va renvoyer du blanc
boutoncouleurecran= tkinter.Button(Fenetre_tkinter,text="Choisir la couleur depuis la caméra",command=ChoisirCouleurEcran)

#On affiche les éléments "de base" qui restent toujours à l'écran
bouton.grid(row=6,column=0,columnspan=3)
label.grid(row=0,column=0,columnspan=3)
radio1.grid(row=5,column=0)
radio2.grid(row=5,column=1)
radio3.grid(row=5,column=2)
#On appelle PowerPointTk pour afficher les élements relatifs au mode de fonctionement 1
PowerPointTk()
Fenetre_tkinter.mainloop()#On affiche la fenetre tkinter

