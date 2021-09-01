#3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
lista=[]
for i in range(4):
    lista.append(float(input(f"Digite o {i+1}º nota: ")))
media=(sum(lista))/(i+1)
print(lista)
print("média final é:",media)


#for lista in lista:
    #soma_das_notas += lista
#media=soma_das_notas/(i+1)
    
#media=((lista[0]+lista[1]+lista[2]+lista[3])/(i+1))

