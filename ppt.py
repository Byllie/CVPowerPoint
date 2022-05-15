import pyautogui
import time
temps=0
pyautogui.FAILSAFE=False

def droite():
    """
    fonction qui exécute la touche flèche droite ("righ") du clavier afin de passer à la slide suivante.
    """
    global temps
    if time.time()-temps>1:
        pyautogui.press('right')
        temps=time.time()
    else:
        pass

def gauche():
    """
    fonction qui exécute la touche flèche gauche ("left") du clavier afin de revenir à la slide précédente.
    """
    global temps
    if time.time()-temps>1:
        pyautogui.press('left')
        temps=time.time()
    else:
        pass


def volumeplus():
    global temps
    if time.time()-temps>1:
        pyautogui.press('volumeup')
        temps=time.time()
    else:
        pass

def volumemoins():
    """
    Fonction qui augmente le volume interne de l'ordinateur.
    """
    global temps
    if time.time()-temps>1:
        pyautogui.press('volumedown')
        temps=time.time()
    else:
        pass

def suivant():
    """
    Fonction qui passe à la musique suivante.
    """
    global temps
    if time.time()-temps>1:
        pyautogui.press('nexttrack')
        temps=time.time()
    else:
        pass

def precedent():
    """
    Fonction qui passe à la musique précédente.
    """
    global temps
    if time.time()-temps>1:
        pyautogui.press('prevtrack')
        temps=time.time()
    else:
        pass

def souris(x,y,taille):
    """
    Fonction qui place le curseur de la souris à la pisition (x, y) donnée en paramètre (utilisé dans le mode "souris").
    """
    tailleecran=pyautogui.size()
    x= (x/taille[0])*tailleecran[0]#on adapte les cordonnées de la camera, en coordonnée de l'écran. 50px sur 100px de la camera =1/2 donc 1040 px sur un écran de 2080px
    y=(y/taille[1])*tailleecran[1]
    pyautogui.moveTo(x,y)
    return None


