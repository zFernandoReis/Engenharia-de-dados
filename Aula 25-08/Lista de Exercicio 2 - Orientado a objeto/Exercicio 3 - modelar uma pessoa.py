'''
3. Classe Pessoa: Crie uma classe que modele uma pessoa:
a. Atributos: nome, idade, peso e altura
b. Métodos: Envelhercer, engordar, emagrecer, crescer. 
Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
'''

class Pessoa():
    def __init__(self,nome, idade, peso, altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
    def envelhecer(self,idade):
        self.idade+=idade
    def engordar(self,peso):
        self.peso+=peso
    def emagrecer(self,peso):
        self.peso -= peso
    def crescer(self,idade):
        if self.idade < 21:
            self.altura += 0.5
pessoa1 = Pessoa("Fernando", 12, 90, 1.78)
pessoa1.engordar(4)
print(pessoa1.peso)
pessoa1.emagrecer(10)
print(pessoa1.peso)
print(pessoa1.idade)
pessoa1.envelhecer(6)
print(pessoa1.idade)
print("===========================")
print(pessoa1.altura)
pessoa1.crescer(pessoa1.idade)
print(pessoa1.altura)






