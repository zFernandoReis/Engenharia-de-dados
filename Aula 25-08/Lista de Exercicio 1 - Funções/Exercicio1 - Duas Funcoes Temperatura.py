#1) Implementar duas funções:
 #Uma que converta temperatura em graus Celsius para Fahrenheit.
 #Outra que converta temperatura em graus Fahrenheit para Celsius.
c=float(input("Digite os graus em celsius: "))
f=float(input("Digite os graus em fahrenheirt: "))

def celsius(c):
    celsius_=(c*(9/5))+32
    return celsius_
def fahrenheirt(f):
  fahrenheirt_=(f-32)*(5/9)
  return fahrenheirt_

print(f"Os graus de Celsius para fahrenheirt é {celsius(c)}")
print(f"Os graus de fahrenheirt para celsius é {fahrenheirt(f)}")


