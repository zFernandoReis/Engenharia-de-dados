class Funcionario():
  def _init_(self, nome,cpf,salario):
    self.nome = nome
    self.cpf = cpf
    self.salario = salario

  def get_bonificacao(self):
    return self.salario * 0.15  

class Gerente(Funcionario):
  def _init_(self, nome, cpf, salario, senha, qtd_funcionarios):
    super()._init_(nome, cpf, salario)
    self.senha = senha
    self.qtd_funcionarios = qtd_funcionarios

  def get_bonificacao(self):
    return super().get_bonificacao() * 2  

joao = Funcionario("João","122555",2500)
andre = Gerente("André", "7526998", 3500, "admin", 25)

print(vars(joao))
print(joao.get_bonificacao())
print(vars(andre))
print(andre.get_bonificacao())