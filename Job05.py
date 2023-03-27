class Animal:

    def __init__(self, prenom, age):
        self.prenom = ""
        self.age = 0
        print("L'âge de l'animal", self.age)
   
    def vieillir(self):
        self.age += 1
        print("L'âge de l'animal", self.age)

    def nommer(self, prenom):
        self.prenom = prenom
        print("L'animal se nomme", prenom)

        
age_animal = Animal("", 0)
name_animal = Animal("", 0)

age_animal.vieillir()
name_animal.nommer("Luna")





    