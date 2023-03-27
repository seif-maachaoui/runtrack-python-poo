class Personne:

    def __init__(self, prenom, nom):
        self.prenom = prenom
        self.nom = nom 

    def SePresenter(self):
        print("Je suis " +  self.prenom + " " + self.nom)

p1 = Personne("John", "Doe")
p2 = Personne("Jean", "Dupond")
p1.SePresenter()
p2.SePresenter()




        


    