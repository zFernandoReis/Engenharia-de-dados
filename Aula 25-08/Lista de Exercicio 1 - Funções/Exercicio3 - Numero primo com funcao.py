#3)Fazer um programa com duas funções, uma para verificar se o número é primo
#e retornar verdadeiro ou falso, e outra para exibir os números primos até chegarem nele
def primo(n):
    for i in range(2,n):
        if (n % i == 0):
            return False
    return True
def exibe():
    n = int(input("Exibir números primos até: "))
    for val in range(2, n+1):
        if(primo(val)):
            print(val)
while True:
    exibe()



