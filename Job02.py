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
        #Lier une classe enfant à son parent
        Personne.__init__(self, age) 

    def allerEnCours(self):
        print("Je vais en cours\n")

class Professeur(Personne):

    def __init__(self, matiereEnseignée, age):
        self.__matiereEnseignée = matiereEnseignée
        Personne.__init__(self, age)

    def enseigner(self):
        print("Le cours va commencer")


    
p1 = Personne(14)
eleve1 = Eleve(15)
prof = Professeur("Philosophie", 40)

eleve1.bonjour()
eleve1.afficherAge()
eleve1.allerEnCours()

prof.bonjour()
prof.afficherAge()
prof.enseigner()

