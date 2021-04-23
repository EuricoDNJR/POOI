class Historico:
    def __init__(self):
        self._hist = []

    @property
    def hist(self):
        return self._hist

    @hist.setter
    def hist(self, hist):
        self._hist = hist

    def exibir(self):
        for operacao in self._hist:
            print(operacao)

    def inserir(self, operacao):
        self._hist.append(operacao)