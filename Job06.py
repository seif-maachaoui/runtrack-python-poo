class Vehicule:
    def __init__(self, marque, année, prix):
        self.marque = marque
        self.année = année
        self.prix = prix

    def informationsVehicule(self, model):
        self.model = model
        print("Marque =", self.marque)
        print("Model =", self.model)
        print("Année =", self.année)
        print("Prix =", self.prix)

class Voiture(Vehicule):
    def __init__(self, marque, model, année, prix, portes):
        Vehicule.__init__(self) 
        self.portes = portes
        
    def informationsVehicule(self):
        Vehicule().informationsVehicule()
        print("Nombre de porte =", self.portes)
    
car = Vehicule("Mercedes", 2020, 18500)
car.informationsVehicule("Classe A")
