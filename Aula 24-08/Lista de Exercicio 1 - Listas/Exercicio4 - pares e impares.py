#4) Faça um Programa que leia 20 números inteiros e armazene-os numa lista. 
# Armazene os números pares na listar PAR e os números IMPARES na lista ímpar. Imprima os três vetores.
lista=[]
par =[] 
impar =[]
for i in range (5):
    x=int(input(f"Digite o {i+1}º número inteiro: "))
    lista.append(x)
    if x%2==0:
        par.append(x)
    else:
        impar.append(x)
print("Todos os numeros inseridos",lista)
print("Numeros pares: ",par)
print("Numeros impares: ",impar)