#2) Faça um Programa que leia uma lista de 10 números reais e mostre-os na ordem inversa.
lista=[]
for i in range(10):
    lista.append(float(input(f"Digite o {i+1}º número real: "))) 
lista.reverse()
print(lista)
