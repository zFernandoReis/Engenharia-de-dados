#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

tupla=("teclado","garrafa","papel","mouse")
lista_total=[]
for i in range(len(tupla)):
    lista=[]
    for x in tupla[i]:
        if x in 'aeiou':
            lista.append(x)
            lista_total.append(x)
    print(f"{tupla[i]}, as vogais presente neste objeto é respectivamente {lista}\n")      
print(f"Todas as vogais presentes na tupla {lista_total}")
