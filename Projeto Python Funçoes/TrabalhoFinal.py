from abc import ABC, abstractclassmethod, abstractmethod
import datetime

class Data():
    @abstractclassmethod
    def dataAtual(self):
        data = datetime.date.today()
        return data

class Pessoa(Data):
    def __init__(self,nome,email,cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf

    def outrosFuncionarios(self,profissao):
        cadastro_ = {}
        cadastro_["nome"] = self.nome
        cadastro_["cpf"] = self.cpf
        cadastro_["email"] = self.email
        cadastro_["Profissão"]=profissao
        return print(cadastro_)

class Visitante(Pessoa):
    def __init__(self,nome,email = '',cpf=''):
        super().__init__(nome,email,cpf)

    def expira(self):
        anoexpira = 1 + int(self.dataAtual().strftime("%Y"))
        print(f'Permissão concedida até {anoexpira}')


class Aluno(Pessoa):
    def __init__(self,nome,email='',cpf='',registroAluno='',materias={},historico=[],__senhadoAluno = ''):
        super().__init__(nome,email,cpf)
        self.registroAluno = registroAluno
        self.materias = materias
        self.historico = historico
        self.__senhadoAluno = __senhadoAluno

    def matricular(self, materia):
        c = 0   # Contador para verificar se a disciplina ja esta matriculada
        for disciplina in self.materias:
            if disciplina == materia:
                c = 1
        if c == 0:
            self.materias[materia]= {'Status':'Cursando', 'Nota1': 0, 'Nota2': 0,
                                     'Media': 0, 'Frequencia':0}

    def desmatricular(self,materia):
        c = 0   # Contador para verificar se a disciplina está matriculada
        for disciplina in self.materias:
            if disciplina == materia:
                c = 1
        if c == 1:
            del self.materias[materia]

    def lancarmentoDisciplina(self, materia, Nota1="None", Nota2="None", Frequencia="None"):
        for i in self.materias:
            if i == materia:
                if Nota1!="None":
                    self.materias[materia]['Nota1'] = Nota1
                if Nota2 != "None":
                    self.materias[materia]['Nota2'] = Nota2
                self.materias[materia]['Media'] = (self.materias[materia]['Nota1']
                                                   +self.materias[materia]['Nota2'])/2
                if Frequencia != "None":
                    self.materias[materia]['Frequencia'] = Frequencia

    def fechamentoDisciplina(self,materia):
        for disciplina in self.materias:
            if disciplina == materia:
                if self.materias[materia]['Media'] >= 60 and \
                        self.materias[materia]['Frequencia'] >= 75:
                    self.materias[materia]['Status'] = 'Aprovado'
                else:
                    self.materias[materia]['Status'] = 'Reprovado'
                self.atualizarHistorico(disciplina)

    def atualizarHistorico(self, disciplina):  #.strftime("%Y"): pega só o ano da data
        self.historico.append({'Ano' : self.dataAtual().strftime("%Y"), 'Disciplina': disciplina,
                               'Media': self.materias[disciplina]['Media'],
                               'Frequencia': self.materias[disciplina]['Frequencia'],
                               'Status': self.materias[disciplina]['Status']})

    def imprimirHistorico(self):
        print('')
        print('-' * 1000)
        print(f'Aluno: {self.nome}\nRegistro: {self.registroAluno}\n\nHistórico Escolar:\n')
        print()
        for i in range(len(self.historico)):
            print(f'|{self.historico[i]["Ano"]}|'
                  f' {self.historico[i]["Disciplina"]} |'
                  f' Média: {self.historico[i]["Media"]:4.1f} |'
                  f' Frequencia: {self.historico[i]["Frequencia"]:4.0f}% |'
                  f' Status: {self.historico[i]["Status"]:9} |')
        print(f'\n\nEmitido em {self.dataAtual()}')
        print('-'*1000)

    def imprimirBoletin(self):
        print('')
        print('-' * 1000)
        print(f'Aluno: {self.nome}\nRegistro: {self.registroAluno}\n\nBoletim:\n')
        for disciplina in self.materias:
            print(f'{disciplina}: Nota1: {self.materias[disciplina]["Nota1"]:4.0f}; '
                  f' Nota2: {self.materias[disciplina]["Nota2"]:4.0f};'
                  f' Media: {self.materias[disciplina]["Media"]:4.1f};'
                  f' Frequencia: {self.materias[disciplina]["Frequencia"]:4.0f}%;'
                  f'     Status: {self.materias[disciplina]["Status"]}')
        print(f'\n\nEmitido em {self.dataAtual()}')
        print('-' * 1000)

    def apagarBoletim(self):
        self.materias = {}

    def loginAluno(self, registroAluno):
        senha = str(input("Digite a senha Desejada: "))
        c = 0
        for i in range(len(senha)):
            if senha[i] in 'qwertyuiopasdfghjklzxcvbnm1234567890':
                c += 1
            else:
                True
                # senha=" "
                # return print("Digite uma senha valida")
        if c == len(senha):
            self.__senhaAluno = senha
            print(f"Login criado, Username:{registroAluno} e senha:{senha}")
        else:
            self.__senhaAluno = ""
            print("Digite uma senha com caracterias alfanumericas")

    def cadastroAluno(self):
        cadastro_ = {}
        cadastro_["nome"] = self.nome
        cadastro_["cpf"] = self.cpf
        cadastro_["email"] = self.email
        cadastro_["Registro do Aluno"] = self.registroAluno
        return print(cadastro_)


class Professor(Pessoa):
    def __init__(self, nome, cpf, email, __senhaProfessor, registroProfessor, valorHora=0,
                 horasTrabalhadas=0):  # ,endereco,email,genero,dataNascimento,telefone=0):                         #,horasTrabalhadas):
        super().__init__(nome, cpf, email)
        self.registroProfessor = registroProfessor
        self.valorHora = valorHora
        self.horasTrabalhadas = horasTrabalhadas
        self.__senhaProfessor = __senhaProfessor

    def cadastroProfessor(self):
        cadastro_ = {}
        cadastro_["nome"] = self.nome
        cadastro_["cpf"] = self.cpf
        cadastro_["email"] = self.email
        cadastro_["Registro do Professor"] = self.registroProfessor
        cadastro_["Valor Hora"] = self.valorHora
        cadastro_["Horas Trabalhadas Mês"] = self.horasTrabalhadas
        return print(cadastro_)

    def salario(self):
        salario_ = self.valorHora * self.horasTrabalhadas
        return print(f'Salario: R${salario_:.2f}')

    def bonificacao(self, formaçãoAcademica):
        salario_ = self.valorHora * self.horasTrabalhadas
        if formaçãoAcademica.lower() == "pos-doutorado":
            salario_ *= 1.30
        elif formaçãoAcademica.lower() == "doutor":
            salario_ *= 1.20
        elif formaçãoAcademica.lower() == "mestre":
            salario_ *= 1.10
        else:
            print("Bônus não aplicado")
        return print(f"Portanto seu salário com bonificação é: R${salario_:.2f}")


    def loginProfessor(self, registroProfessor):
        senha = str(input("Digite a senha Desejada: "))
        c = 0
        for i in range(len(senha)):
            if senha[i] in 'qwertyuiopasdfghjklzxcvbnm1234567890':
                c += 1
            else:
                True
                # senha=" "
                # return print("Digite uma senha valida")
        if c == len(senha):
            self.__senhaProfessor = senha
            print(f"Login criado, Username:{registroProfessor} e senha:{senha}")
        else:
            self.__senhaProfessor = ""
            print("Digite uma senha com caracteres alfanumericas")

Pessoa1=Pessoa("dasda","@Dsadsada","42342342")
Pessoa1.outrosFuncionarios("coordenadora")




#Visitante1 = Visitante('Igor G.', '@prof.com','487538475')
# print(vars(Visitante1))
# Visitante1.expira()


#Aluno1 = Aluno('Isis Valverde','@isisvalverde.com','489353458745','20217364362',{},[],'')
# # print(vars(Aluno1))
# # Professo1 = Professor('Bis','@bis.com','4753447','','2021785476387',1000,160)
# # print(vars(Professo1))
# # Aluno2 = Aluno('Jose Maria','@zemaria.com','3876243755','20214985384',{},[],'')
# # print(vars(Aluno2))
# # Aluno1.matricular('Por')
# # Aluno1.imprimirBoletin()
# # Aluno1.matricular('Mat')
# # Aluno1.matricular('Geo')
# # Aluno1.lancarmentoDisciplina('Por',Nota1 = 80, Frequencia = 75)
# # Aluno1.lancarmentoDisciplina('Por',Nota2=70)
# # Aluno1.lancarmentoDisciplina('Mat',70,90,80)
# # Aluno1.fechamentoDisciplina('Por')
# # Aluno1.fechamentoDisciplina('Mat')
# # Aluno1.desmatricular('Geo')
# # Aluno1.apagarBoletim()
# # Aluno1.imprimirBoletin()
# # Aluno1.loginAluno('20217364362')
#Aluno1.cadastroAluno()
# # Aluno1.imprimirHistorico()

#Professor1 = Professor('Bis','@bis.com','4753447','','2021785476387',50,160)
#Professor1.cadastroProfessor()
#Professor1.loginProfessor('423423423')
#Professor1.loginProfessor('423423423')
#Professor1.salario()
#Professor1.bonificacao('Mestre')

