import pyautogui
import time
mode_de_fonctionnemnt=0
temps=0
def mouvement(mouv):
    global temps
    global mode_de_fonctionnemnt
    if mode_de_fonctionnemnt==0:
        if time.time()-temps>1:
            if mouv=="Bras-Droit":
                pyautogui.press('left')
            elif mouv=="Bras-Gauche":
                pyautogui.press('right')
            if type(mouv)==int:
                mode_de_fonctionnemnt=mouv
            temps=time.time()
    else:
        pass
