class Rectangle :
    def __init__(self, longueur, largeur):
        self.__longueur = 10
        self.__largeur = 5

    def set_longueur(self, longueur):
        self.__longueur = longueur
        return  self.__longueur
    
    def get_longueur(self):
        return self.__longueur
    
    def set_largeur(self, largeur):
        self.__largeur = largeur
        return self.__largeur
    
    def get_largeur(self):
        return self.__largeur
    
rectangle1 = Rectangle(10, 5)

print("La longueur actuelle est de", rectangle1.get_longueur(), "cm")
rectangle1.set_longueur(20)
print("La nouvelle longueur est de", rectangle1.get_longueur(), "cm")

print("La largeur actuelle est de", rectangle1.get_largeur(), "cm")
rectangle1.set_largeur(30)
print("La nouvelle largeur est de", rectangle1.get_largeur(), "cm")





    