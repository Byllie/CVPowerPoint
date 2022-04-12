import pyautogui
import time
temps=0

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
