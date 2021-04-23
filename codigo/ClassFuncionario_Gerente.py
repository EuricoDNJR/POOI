from ClassPessoa import Pessoa
from ClassLogin import Login


class Funcionario(Pessoa, Login):

    def __init__(self, codigo, nome, endereco, telefone, cpf, rg, senha):
        Pessoa.__init__(self, codigo, nome, endereco, telefone, cpf, rg)
        Login.__init__(self, senha)
        self._permissao_total = False

    @property
    def permissao_total(self):
        return self._permissao_total

    def altera(self, nome, endereco, telefone, cpf, rg):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cpf = cpf
        self._rg = rg
        senha = input("Insira a nova senha: ")
        self._senha = senha


class Gerente(Pessoa, Login):

    def __init__(self, codigo, nome, endereco, telefone, cpf, rg, senha):
        Pessoa.__init__(self, codigo, nome, endereco, telefone, cpf, rg)
        Login.__init__(self, senha)
        self._permissao_total = True

    @property
    def permissao_total(self):
        return self._permissao_total

    def altera(self, nome, endereco, telefone, cpf, rg):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cpf = cpf
        self._rg = rg
        senha = input("Insira a nova senha: ")
        self._senha = senha