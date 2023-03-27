from Job01 import Operation

class Operation:

    def __init__(self, nombre1, nombre2): 
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def initial_number(self):
        print("Le nombre1 est", self.nombre1)
        print("Le nombre2 est", self.nombre2)
    
    
set_number = Operation(12, 15)
set_number.nombre2 = 3
set_number.initial_number()



