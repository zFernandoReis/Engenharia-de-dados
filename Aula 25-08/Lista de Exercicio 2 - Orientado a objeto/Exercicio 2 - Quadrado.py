'''
Modelar um quadrado com seguintes parametros:
Atributos: lado
Métodos: Mudar valor do lado, Retornar valor do lado e calcular  Area

'''
class Quadrado():
    def __init__(self,lado):
        self.lado=lado
    def trocalado(self,lado):
        self.lado=lado
    def getlado(self):
        return self.lado
    def area(self):
        return self.lado **2
q= Quadrado(5)
print(q.getlado())
print(q.area())
q.trocalado(8)
print(q.getlado())
print(q.area())
