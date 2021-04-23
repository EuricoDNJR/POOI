class Conta_a_Pagar:

    def __init__(self, codigo, cod_reabastecimento, valor, data_pagamento):
        self._codigo = codigo
        self._cod_reabastecimento = cod_reabastecimento
        self._valor = valor
        self._data_pagamento = data_pagamento

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def cod_reabastecimento(self):
        return self._cod_reabastecimento

    @cod_reabastecimento.setter
    def cod_reabastecimento(self, cod_reabastecimento):
        self._cod_reabastecimento = cod_reabastecimento

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, valor):
        self._valor = valor

    @property
    def data_pagamento(self):
        return self._data_pagamento

    @data_pagamento.setter
    def data_pagamento(self, data_pagamento):
        self._data_pagamento = data_pagamento