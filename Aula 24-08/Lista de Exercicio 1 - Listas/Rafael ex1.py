lista = []
for n in range(5):
    while True:
        try:
            num = int(input(f'Digite o {n+1}º número: '))
            lista.append(num)
            break
        except:
            print('\nDigite apenas número inteiro!\n')
print(lista)