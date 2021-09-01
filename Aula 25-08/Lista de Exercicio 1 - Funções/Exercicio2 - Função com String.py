#2) Escreva uma função que:
 #Receba uma frase como parâmetro.
 #Retorne uma nova frase com cada palavra com as letras invertidas

def inverter(frase):
    return frase[::-1]
x=str(input("Digite uma frase: "))
print(inverter(x))



