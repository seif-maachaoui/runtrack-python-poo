class Forme:
    def aire(self, longueur, largeur):
        return 0
    
class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        Forme.__init__(self)
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self):
        return self.longueur * self.largeur
rect = Rectangle(5, 10)
print("Le résultat de la méthode aire est", rect.aire())
