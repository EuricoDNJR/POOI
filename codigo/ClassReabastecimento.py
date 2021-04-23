class Reabastecimento:

    def __init__(self, codigo, cod_fornecedor, cod_produto, cod_gerente, valor, quantidade):
        self._codigo = codigo
        self._cod_produto = cod_produto
        self._cod_fornecedor = cod_fornecedor
        self._cod_gerente = cod_gerente
        self._valor = valor
        self._quantidade = quantidade

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def cod_fornecedor(self):
        return self._cod_fornecedor

    @cod_fornecedor.setter
    def cod_fornecedor(self, cod_fornecedor):
        self._cod_fornecedor = cod_fornecedor

    @property
    def cod_gerente(self):
        return self._cod_gerente

    @cod_gerente.setter
    def cod_gerente(self, cod_gerente):
        self._cod_gerente = cod_gerente

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade
