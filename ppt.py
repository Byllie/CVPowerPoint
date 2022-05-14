import pyautogui
import time
temps=0
pyautogui.FAILSAFE=False

def droite():
    global temps
    if time.time()-temps>1:
        pyautogui.press('right')
        temps=time.time()
    else:
        pass

def gauche():
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
    global temps
    if time.time()-temps>1:
        pyautogui.press('volumedown')
        temps=time.time()
    else:
        pass

def suivant():
    global temps
    if time.time()-temps>1:
        pyautogui.press('nexttrack')
        temps=time.time()
    else:
        pass

def precedent():
    global temps
    if time.time()-temps>1:
        pyautogui.press('prevtrack')
        temps=time.time()
    else:
        pass

def souris(x,y,taille):
    tailleecran=pyautogui.size()
    print(x,y,taille,tailleecran)
    x=x/taille[0]*tailleecran[0]
    y=x/taille[1]*tailleecran[1]
    print(x,y)
    pyautogui.moveTo(y,x)
    return None
