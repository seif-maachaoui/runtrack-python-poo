import math

class Forme:
    def aire(self, longueur, largeur, radius):
        return 0

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        Forme.__init__(self)
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self):
        return self.longueur * self.largeur
    

class Cercle(Forme):
    def __init__(self, radius):
        Forme.__init__(self)
        self.radius = radius

    def aire(self):
        return self.radius**2 * math.pi

rect = Rectangle(5, 10)
cercle = Cercle(4)

print("Le résultat de la méthode aire, pour le rectangle est de", rect.aire(), "cm")
print("le résultat de la méthode aire, pour le Cercle est de", cercle.aire(), "cm")
