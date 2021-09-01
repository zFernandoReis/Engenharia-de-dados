'''
1. Classe Bola: Crie uma classe que modele uma bola:
a. Atributos: Cor, circunferência, material
b. Métodos: trocaCor e mostraCor
'''


class bola():
    def __init__(self,cor,circuferencia, material):
        self.cor=cor
        self.circuferencia=circuferencia
        self.material=material
    def trocaCor(self,cor):
        self.cor = cor
        
    def mostraCor(self):
        return self.cor

bola1 = bola("Azul", 20,"couro")
print(bola1.mostraCor())

bola1.trocaCor("Vermelha")
print(bola1.mostraCor())
        