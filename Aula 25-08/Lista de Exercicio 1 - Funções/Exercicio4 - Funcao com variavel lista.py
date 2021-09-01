#4) Implementar uma função que receba uma lista de listas de comprimentos quaisquer 
 #e retorne uma lista de uma dimensão.

def listaDimensao(listaInserir):
    listaDimensao = []
    for lista in listaInserir:
        for elemento in lista:
            listaDimensao.append(elemento)
        print(listaDimensao)
lista1=[[2.4], [7], [8]]
listaDimensao(lista1)
    
    