class Rectangle: 
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def périmètre(self):
        result_périmètre = self.__longueur + self.__largeur * 2
        print("\nLe périmètre du rectangle est égal à", result_périmètre)

    def surface(self):
        result_surface = self.__longueur * self.__largeur
        print("La surface du rectangle est égal à", result_surface)

    def set_longueur(self, longueur):
        self.__longueur = longueur
        return self.__longueur

    def get_longueur(self):
        return self.__longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
        return self.__largeur
    
    def get_largeur(self):
        return self.__largeur
    
class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.hauteur = hauteur

    def volume(self):
        result_volume = self._Rectangle__longueur * self._Rectangle__largeur * self.hauteur
        print("Le volume du rectangle est égal à", result_volume)



rect = Rectangle (5, 10)
parall = Parallélépipède(10, 20, 5)

#Longueur du rectangle
print("La longueur actuelle est de", rect.get_longueur(), "cm")
rect.set_longueur(10)
print("La nouvelle longueur est de", rect.get_longueur(), "cm\n")

#Largeur du rectangle
print("La largeur actuelle est de", rect.get_largeur(), "cm")
rect.set_largeur(20)
print("La nouvelle largeur est de", rect.get_largeur(), "cm\n")

rect.périmètre()
rect.surface()
parall.volume()
