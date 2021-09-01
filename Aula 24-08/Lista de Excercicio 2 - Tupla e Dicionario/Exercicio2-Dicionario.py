# Faça um programa que leia nome e média de um aluno, guardando também a situção 
#em um dicionário. No final,
# mostre o conteúdo da estrutura na tela.
dicionario={}
i=0
laço=""
while laço != "n":
    laço=str(input("Digite (y) para adicionar um aluno ou (n) para parar a aplicação: "))
    if laço == "y":
        dicionario[f"nome_{i+1}"]=str(input("Digite o seu nome: "))
        dicionario[f"media_{i+1}"]=float(input("Digite a sua média: "))
        if dicionario[f"media_{i+1}"] >= 6:
            dicionario[f"Situação_{i+1}"]="Aprovado"
        else:
            dicionario[f"Situação_{i+1}"]="Reprovado"
        i+=1
    if laço == "n":
        print("Valores adicionados", dicionario)