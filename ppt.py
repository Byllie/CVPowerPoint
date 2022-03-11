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
