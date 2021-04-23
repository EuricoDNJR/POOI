import abc
from ClassHistorico import Historico


class Pessoa(abc.ABC):
    def __init__(self, codigo, nome, endereco, telefone, cpf, rg):
        self._codigo = codigo
        self._nome = nome
        self._endereco = endereco
        self._telefone = telefone
        self._cpf = cpf
        self._rg = rg
        self._historico = Historico()

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf

    @property
    def rg(self):
        return self._rg

    @rg.setter
    def rg(self, rg):
        self._rg = rg

    @property
    def historico(self):
        return self._historico

    @abc.abstractmethod
    def altera(self, nome, endereco, telefone, cpf, rg):
        pass
