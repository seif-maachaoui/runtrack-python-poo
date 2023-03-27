from Job02 import Operation 

class Operation :
        
    def __init__(self, nombre1, nombre2): 
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    
    def sum(self):
        result = self.nombre1 + self.nombre2
        print("La somme des 2 nombres est", result)

sum_number = Operation(12, 3)
sum_number.sum()
