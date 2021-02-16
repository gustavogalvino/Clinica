from abc import ABC, abstractmethod


class Clinica():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco
        self.funcionarios = {}

    def incluir_funcionarios(self, funcionario, funcao):
        self.funcionarios[funcionario] = funcao

    def exibir_funcionarios(self):
        for f in self.funcionarios:
            print(f"Funcionário: {f}")
            print(f"Função: {self.funcionarios[f]}")
            print(30 * "-")


class Pessoa(ABC):
    def __init__(self, nome, cpf, rg, telefone):
        self.nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone

    def set_cpf(self, cpf):
        self.__cpf = cpf

    def set_rg(self, rg):
        self.__rg = rg

    def set_telefone(self, telefone):
        self.__telefone = telefone

    def get_cpf(self):
        return self.__cpf

    def get_rg(self):
        return self.__rg

    def get_telefone(self):
        return self.__telefone

    @abstractmethod
    def informacoes(self):
        pass

    @abstractmethod
    def assinatura(self):
        pass


class Funcionario(Pessoa):
    def __init__(self, nome, cpf, rg, telefone, salario):
        self.nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone
        self.__salario = salario

    def set_salario(self, salario):
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.__cpf}")
        print(f"RG: {self.__rg}")
        print(f"Telefone: {self.__telefone}")
        print(f"Salário: R$ {self.__salario}")
        print(30 * "-")

    def assinatura(self):
        print(f"Ass.: {self.nome}\n      {self.__cpf}")

    def get_assinatura(self):
        return (f"Ass.: {self.nome}\n      {self.__cpf}")


class Medico(Funcionario):
    def __init__(self, nome, cpf, rg, telefone, salario, crm):
        self.nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone
        self.__salario = salario
        self.__crm = crm
        self.__especialidades = []

    def set_crm(self, crm):
        self.__crm = crm

    def incluir_especialidade(self, especialidade):
        self.__especialidades.append(especialidade)

    def get_crm(self):
        return self.__crm

    def get_especialidades(self):
        return self.__especialidades

    def informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.__cpf}")
        print(f"RG: {self.__rg}")
        print(f"CRM: {self.__crm}")
        print(f"Telefone: {self.__telefone}")
        print(f"Especialidades: {self.__especialidades}")
        print(f"Salário: R$ {self.__salario}")
        print(30 * "-")

    def assinatura(self):
        print(f"Ass.: {self.nome}\n      {self.__crm}")

    def get_assinatura(self):
        return (f"Ass.: {self.nome}\n      {self.__crm}")


class Paciente(Pessoa):
    def __init__(self, nome, cpf, rg, telefone, endereco, data_nascimento):
        self.nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__telefone = telefone
        self.__endereco = endereco
        self.__data_nascimento = data_nascimento
        self.__num_convenio = None
        self.__responsavel = None
        self.__historico = {}

    def set_endereco(self, endereco):
        self.__endereco = endereco

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento

    def set_num_convenio(self, num_convenio):
        self.__num_convenio = num_convenio

    def set_responsavel(self, responsavel):
        self.__responsavel = responsavel

    def get_endereco(self):
        return self.__endereco

    def get_data_nascimento(self):
        return self.__data_nascimento

    def get_num_convenio(self):
        return self.__num_convenio

    def get_responsavel(self):
        return self.__responsavel

    def informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.__cpf}")
        print(f"RG: {self.__rg}")
        print(f"Data de Nascimento: {self.__data_nascimento}")
        print(f"Telefone: {self.__telefone}")
        print(f"Endereço: {self.__endereco}")
        if self.__num_convenio is None:
            print("Não Conveniado.")
        else:
            print(f"Número do Convênio: {self.__num_convenio}")
        print(f"Médico Responsável: {self.__responsavel}")
        print(30 * "-")

    def assinatura(self):
        print(f"Ass.: {self.nome}\n      {self.__cpf}")

    def get_assinatura(self):
        return (f"Ass.: {self.nome}\n      {self.__cpf}")

    def adiciona_historico(self, lista):
        self.__historico[lista[0]] = lista[1]

    def exibe_chaves(self):
        for c in self.__historico:
            print(c)

    def historico_completo(self):
        for c in self.__historico:
            print(c, ":", self.__historico[c])

    def exibe_historico(self, chave):
        print(self.__historico[chave])


class Quarto():
    def __init__(self, andar, numero):
        self.andar = andar
        self.numero = numero
        self.__paciente = None

    def set_paciente(self, paciente):
        self.__paciente = paciente

    def informacoes_quarto(self):
        print(f"Andar: {self.andar}º")
        print(f"Número: {self.numero}")
        if self.__paciente is not None:
            print("Paciente:")
            self.__paciente.informacoes()
        else:
            print("Quarto vazio.")


class Historico():
    def __init__(self, data, horario, observacao, responsavel):
        self.data = data
        self.horario = horario
        self.observacao = observacao
        self.responsavel = responsavel
        self.lista = []

    def adiciona_observacao(self):
        chave = self.data + " - " + self.horario
        self.lista.append(chave)
        obs = self.observacao + "\n" + self.responsavel
        self.lista.append(obs)

    def get_lista(self):
        return self.lista
