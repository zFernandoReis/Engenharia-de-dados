num1=float(input("digite numero para ser calculado: "))
num2=float(input("digite outro para ser calculado: "))
op=str(input("digite a operação desejada: "))

class Calculadora():
    def __init__(self, num1,num2,result=0):
        self.num1=num1
        self.num2=num2
        self.result=result
    def soma(self,num1,num2):
        self.result = self.num1 + self.num2
    def sub(self,num1,num2):
        self.result=self.num1 - self.num2
    def multi(self,num1,num2):
        self.result=self.num1 * self.num2
    def div(self,num1,num2):
        self.result=self.num1 / self.num2

calculo=Calculadora(num1,num2)

if op == "+":
    calculo.soma(num1, num2)  
elif op == "-":
    calculo.sub(num1,num2)
elif op == "*":
    calculo.multi(num1,num2)
elif op == "/":
    calculo.div(num1,num2)
else:
    print("Digite um simbolo de operação valida")    
print(calculo.result)


x = {}
print(type(x))
    