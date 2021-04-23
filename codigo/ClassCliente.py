from ClassPessoa import Pessoa
from ClassHistorico import Historico


class Cliente(Pessoa):

    def __init__(self, codigo, nome, endereco, telefone, cpf, rg):
        super().__init__(codigo, nome, endereco, telefone, cpf, rg)
        self._historico = Historico()

    @property
    def historico(self):
        return self._historico

    def altera(self, nome, endereco, telefone, cpf, rg):
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cpf = cpf
        self._rg = rg
