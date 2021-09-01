'''
4. Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista 
e saldo. Os métodos são os seguintes: alterarNome, depósito e saque; 
No construtor, saldo é opcional, com valor default zero e os demais 
atributos são obrigatórios.
'''
class Conta():
    def __init__(self,num_conta, nome_correntista,saldo=0):
        self.num_conta=num_conta
        self.nome_correntista=nome_correntista
        self.saldo=saldo

    def alterarNome(self,nome_correntista):
        self.nome_correntista=nome_correntista
        
    def deposito(self,saldo):
        self.saldo+=saldo
        
    def saque(self,saldo):
        if self.saldo == 0:
            print("Saldo zerado")
        else:
            self.saldo-=saldo

        
conta1 = Conta("3123123","Fernando")
print(vars(conta1))
print(conta1.saldo)
conta1.deposito(100)
print(conta1.saldo)
conta1.saque(50)
print(conta1.saldo)




