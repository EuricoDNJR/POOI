class Produto:

    def __init__(self, codigo, valor_venda, nome_produto, categoria, descricao):
        self._codigo = codigo
        self._valor_compra = 0.0
        self._valor_venda = valor_venda
        self._nome_produto = nome_produto
        self._categoria = categoria
        self._descricao = descricao
        self._quantidade = 0

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def valor_compra(self):
        return self._valor_compra

    @valor_compra.setter
    def valor_compra(self, valor_compra):
        self._valor_compra = valor_compra

    @property
    def valor_venda(self):
        return self._valor_venda

    @valor_venda.setter
    def valor_venda(self, valor_venda):
        self._valor_venda = valor_venda

    @property
    def nome_produto(self):
        return self._nome_produto

    @nome_produto.setter
    def nome_produto(self, nome_produto):
        self._nome_produto = nome_produto

    @property
    def categoria(self):
        return self._categoria

    @categoria.setter
    def categoria(self, categoria):
        self._categoria = categoria

    @property
    def descricao(self):
        return self._descricao

    @descricao.setter
    def descricao(self, descricao):
        self._descricao = descricao

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade

    def altera(self, valor_compra, valor_venda, nome_produto, categoria, descricao):
        self._valor_compra = valor_compra
        self._valor_venda = valor_venda
        self._nome_produto = nome_produto
        self._categoria = categoria
        self._descricao = descricao

    def adiciona_quantidades(self, quantidades):
        self._quantidade += quantidades
