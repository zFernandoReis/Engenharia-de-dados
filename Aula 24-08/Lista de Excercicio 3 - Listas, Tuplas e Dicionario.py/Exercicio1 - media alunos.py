#1) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene 
 #numa lista a média
 #de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

media=[]
Aprovados=[]
Reprovados=[]
for i in range (3):
    nome=str(input(f"{i+1}º aluno digite o seu nome: "))
    nota=[]
    for x in range(4):
        nota.append(float(input(f"Digite a {x+1}º nota: ")))
    media.append(sum(nota)/(x+1))
    if media[i] >= 7:
        Aprovados.append(nome)
    else:
        Reprovados.append(nome)
print(f"Os alunos aprovados no conceito final foram {Aprovados}")
print(f"Os alunos reprovados no conceito final foram {Reprovados}")



    

        
