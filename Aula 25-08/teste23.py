from abc import ABC, abstractclassmethod
import datetime

class data():
    @abstractclassmethod
    def dataAtual(self):
        data = datetime.date.today()
        return data

class A(Letras):
    def __init__(self, descricao):
        self.descricao = descricao

    def imprimir(self):
        print('Aqui é um metodo da classe A!')


exemplo_Letra = A("Letra A")
exemplo_Letra.dataAtual()
exemplo_Letra.imprimir()