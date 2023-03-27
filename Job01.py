class Operation: #Création de la classe

    #Chaque classe doit posséder une fonction d'initialisation
    #Le paramètre Self est utilisé pour indiquer que les attributs appartiennent à la classe Operation
    #On place les attributs en paramètre
    def __init__(self, nombre1, nombre2): 
        self.nombre1 = nombre1
        self.nombre2 = nombre2
operation1 = Operation(12, 15)
print(operation1) #On renvoie La classe Operation avec pour attributs 12 et 15


    
