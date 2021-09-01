'''
CRIAR CÓDIGO
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:
a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma 
certa quantidade de combustível no tanque.
b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo o nível de combustível no tanque de gasolina.
d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
e. Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:
consumo = 10 km/l --- andou 10 km--- logo comb_tanque - 1 litro
'''
class Carro():
    def __init__(self,comb_consumo,comb_tanque=0):
        self.comb_consumo=comb_consumo
        self.comb_tanque=comb_tanque
    def andar(self,dist):
        if self.comb_tanque != 0:
            self.comb_tanque-=(dist/self.comb_consumo)
        else:
            print("Adicione Gasolina!!!")
    def obterGasolina(self):
        return print(self.comb_tanque)
    def adicionarGasolina(self,qtd):
        self.comb_tanque+=qtd

fiat = Carro(10,100)
fiat.andar(200)
fiat.adicionarGasolina(20)
fiat.andar(200)
fiat.obterGasolina()







'''
print(fiat.obterGasolina())
print(fiat.comb_tanque)
fiat.adicionarGasolina(2)
print(fiat.comb_tanque)
fiat.obterGasolina()
'''

    
