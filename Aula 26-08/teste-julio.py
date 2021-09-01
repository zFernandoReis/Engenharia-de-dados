from abc import ABC, abstractclassmethod, abstractmethod

class Letras(ABC):
    @abstractmethod
    def __init__(self,ano=0):
        self.ano = ano

    # @abstractmethod
    def mostrarTipo(self):
        print('Eu sou uma classe abstrata')

class Cadastro(Letras):
    def __init__(self, nome, cpf, endereco):
        self.nome = nome
        self.cpf = cpf
        self.endereco = endereco

    def criarCadastro(self):
        cadastro_ = {}
        cadastro_["nome"] = self.nome
        cadastro_["cpf"] = self.cpf

        return print(cadastro_)


class Professor(Cadastro):
    def __init__(self, nome, cpf, endereco, valorHora):
        super().__init__(nome, cpf, endereco)
        self.valorHora = valorHora

    def cadastroProfessor():
        super().criarCadastro()
        cadastro_["Valor Hora"] = self.valorHora
        return print(cadastro_)

Professor1 = Professor('eu','4995','aqui',80)
print(vars(Professor1))
