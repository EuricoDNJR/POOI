from ClassHistorico import Historico


class Fornecedor:

    def __init__(self, codigo, nome, cnpj, email, telefone):
        self._codigo = codigo
        self._nome = nome
        self._cnpj = cnpj
        self._email = email
        self._telefone = telefone
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
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, cnpj):
        self._cnpj = cnpj

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, telefone):
        self._telefone = telefone

    @property
    def historico(self):
        return self._historico

    def altera(self, nome, cnpj, email, telefone):
        self._nome = nome
        self._cnpj = cnpj
        self._email = email
        self._telefone = telefone
