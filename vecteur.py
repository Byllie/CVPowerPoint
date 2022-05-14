import math
class Vecteur:
    """
    Classe qui traite les vecteurs de déplacement entre le point de la main droite de l'image n et n-1. Ces vecteurs sont représentés grâce aux nombre complexes pour des questions de simplicité et également parce que c'est stylé.
    """ 
    def __init__(self,a,b):
        """"
        Constructeur de la clase Vecteur. Ainsi, cela crée le vecteur AB allant du point a au point b donnés en paramètre.
        """
        self.a=a[0]+a[1]*1j
        self.b=b[0]+b[1]*1j
        self.affixe=self.b-self.a
        self.module=math.sqrt(self.affixe.real**2+self.affixe.imag**2)
        self.argument=math.acos(self.affixe.real/self.module) if (math.acos(self.affixe.real/self.module) * math.asin(self.affixe.imag/self.module)>=0) else math.acos(self.affixe.real/-self.module)+math.pi
        #vraiment impresionnant je suis vraiment le roi du sinus (Gwendal) / Pffff, il fait vraiment le fou c'ui là... (Joseph)

class Deplacement:
    """
    Classe qui traite des déplacement représentés par les vecteurs de la classe ci-dessus.
    """
    def __init__(self,angleGrandVecteur,anglePetitVecteur,andor,fonctionmouvement):
        """
        Constructeur de la classe Deplacement qui permet ainsi de savoir si oui ou non une action doit être déclanchée, et si oui la quelle.
        """
        self.a1=angleGrandVecteur
        self.a2=anglePetitVecteur
        self.f=fonctionmouvement
        self.andor=andor
