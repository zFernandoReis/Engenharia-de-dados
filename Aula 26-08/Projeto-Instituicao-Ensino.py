from abc import ABC, abstractclassmethod

class data():
    @abstractclassmethod
    def algumafuncao(self):
        return print("so com print eu funciono")
    def mostrarCadastro(self):
        return cadastro_

class Pessoa():
    def __init__(self,nome,cpf,email):                            #,email,genero,dataNascimento,telefone=0):
        self.nome=nome
        self.cpf=cpf
        self.email=email

class Professor(Pessoa):
    def __init__(self,nome,cpf,email,__senhaProfessor,registroProfessor,valorHora=0,horasTrabalhadas=0):#,endereco,email,genero,dataNascimento,telefone=0):                         #,horasTrabalhadas):
        super().__init__(nome,cpf,email) 
        self.registroProfessor=registroProfessor
        self.valorHora=valorHora
        self.horasTrabalhadas=horasTrabalhadas
        self.__senhaProfessor=__senhaProfessor

    def cadastroProfessor(self):
        cadastro_={}
        cadastro_["nome"]=self.nome
        cadastro_["cpf"]=self.cpf
        cadastro_["email"]=self.email
        cadastro_["Registro do Professor"]=self.registroProfessor
        cadastro_["Valor Hora"]=self.valorHora
        cadastro_["Horas Trabalhadas Mês"]=self.horasTrabalhadas
        return print(cadastro_)

    def salario(self):
        salario_=self.valorHora*self.horasTrabalhadas
        return print(salario_)

    def bonificacão(self, formaçãoAcademica):
        salario_=self.valorHora*self.horasTrabalhadas
        if formaçãoAcademica.lower() == "pos-doutorado":
            salario_ *= 1.30
        elif formaçãoAcademica.lower() == "doutor":
            salario_ *= 1.20
        elif formaçãoAcademica.lower() == "mestre":
            salario_ *= 1.10
        else:
            print("Bônus não aplicado")
        return print(f"Portanto seu salário é:{salario_}" )

    

    def loginProfessor(self, registroProfessor):
        senha=str(input("Digite a senha Desejada: "))
        c=0
        for i in range(len(senha)):
            if senha[i] in 'qwertyuiopasdfghjklzxcvbnm1234567890':
                c+=1
            else:
                True
                #senha=" "
                #return print("Digite uma senha valida")
        if c == len(senha):
            self.__senhaProfessor=senha
            print(f"Login criado, Username:{registroProfessor} e senha:{senha}")
        else:
            self.__senhaProfessor=""
            print("Digite uma senha com caracterias alfanumericas")






######### metodos para Classe aluno
    def loginAluno(self, registroAluno):
        senha=str(input("Digite a senha Desejada: "))
        c=0
        for i in range(len(senha)):
            if senha[i] in 'qwertyuiopasdfghjklzxcvbnm1234567890':
                c+=1
            else:
                True
                #senha=" "
                #return print("Digite uma senha valida")
        if c == len(senha):
            self.__senhaAluno=senha
            print(f"Login criado, Username:{registroAluno} e senha:{senha}")
        else:
            self.__senhaAluno=""
            print("Digite uma senha com caracterias alfanumericas")

    def cadastroAluno(self):
        cadastro_={}
        cadastro_["nome"]=self.nome
        cadastro_["cpf"]=self.cpf
        cadastro_["email"]=self.email
        cadastro_["Registro do Aluno"]=self.registroAluno
        return print(cadastro_)
        
        
cadastro1=Professor("Fernando","31232121","@312321","3123213123")

#cadastro1.criarLogin("dsdas@fgfdfd")
#print(cadastro1.__senha)
print(vars(cadastro1))
#cadastro1.cadastroProfessor()







'''
class Aluno(Cadastro):
    def __init__(self,registroAluno,nivelEscolar,turno):
        super().__init__(endereco, nome, email,sexo,dataNascimento,telefone,cpf)
        self.registroAluno=registroAluno
        self.nivelEscolar=nivelEscolar
        self.turno=turno  
        self.materiasCursadas=materiasCursadas
        self.anoLetivo=anoLetivo
        self.senhaAluno=senhaAluno
    def matricularAluno(self,materia):
        self.materiasCursadas = materia
    def materiasMatriculadas(self):
        return print(self.materiasCursadas)
    '''
    




