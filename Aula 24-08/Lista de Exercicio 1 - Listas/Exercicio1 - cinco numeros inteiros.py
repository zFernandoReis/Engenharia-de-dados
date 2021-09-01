#1) Faça um Programa que leia uma lista de 5 números inteiros e mostre-os.
lista=[]
for i in range(5):
    lista.append(int(input(f"Digite {i+1}º numero inteiro: ")))
    
print(lista)