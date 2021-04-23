class Login:

    def __init__(self, senha):
        self._senha = senha

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha