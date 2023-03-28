class Personne :

    #fonction Constructeur 
    def __init__(self, age):
        self.age = age

    def afficherAge(self):
        print("J'ai", self.age, "ans")
    
    def bonjour(self):
        print("Hello")

    def modifierAge(self):
        self.age = input("Veuillez entrer votre âge :")
        if self.age.isdigit():
            print("J'ai", self.age, "ans\n")
            return self.age
        else:
            print("Erreur, veuillez entrer un âge valide\n")
        return None
    
class Eleve (Personne) :

    def __init__(self, age):
        Personne.__init__(self, age) 

    def allerEnCours(self):
        print("Je vais en cours")

class Professeur():

    def __init__(self, matiereEnseignée):
        self.__matiereEnseignée = matiereEnseignée

    def enseigner(self):
        print("\nLe cours va commencer")


    
p1 = Personne(14)
eleve1 = Eleve(12)
prof = Professeur("Philosophie")

p1.afficherAge()
p1.modifierAge()

eleve1.allerEnCours()
eleve1.afficherAge()

prof.enseigner()

        
