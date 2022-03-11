import math
class Vecteur:
    def __init__(self,a,b):
        self.a=a[0]+a[1]*1j
        self.b=b[0]+b[1]*1j
        self.affixe=self.b-self.a
        self.module=math.sqrt(self.affixe.real**2+self.affixe.imag**2)
        self.argument=math.acos(self.affixe.real/self.module) if (math.acos(self.affixe.real/self.module) *math.asin(self.affixe.imag/self.module)>=0) else math.acos(self.affixe.real/-self.module)+math.pi
        #vraiment impresionnant je suis vraiment le roi du sinus (Gwendal)
class Deplacement:
    def __init__(self,angleGrandVecteur,anglePetitVecteur,andor,fonctionmouvement):
        self.a1=angleGrandVecteur
        self.a2=anglePetitVecteur
        self.f=fonctionmouvement
        self.andor=andor
