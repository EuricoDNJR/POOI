from ClassProduto import Produto
from ClassFornecedor import Fornecedor
from ClassReabastecimento import Reabastecimento
from ClassConta_a_Pagar import Conta_a_Pagar
from ClassFuncionario_Gerente import Funcionario, Gerente
from ClassCliente import Cliente
from datetime import datetime
from datetime import date


def retorna_tempo_atual():
    data_e_hora_atuais = datetime.now()
    data_e_hora_em_texto = data_e_hora_atuais.strftime('%d/%m/%Y %H:%M')
    return data_e_hora_em_texto


def retorna_daqui_a_ndias(n):
    hj = date.today()
    futuro = date.fromordinal(hj.toordinal() + n)  # hoje + n dias
    return futuro


class Sistema:
    def __init__(self):
        self._clientes = []
        self._funcionarios = []
        self._gerentes = []
        self._produtos = []
        self._fornecedores = []
        self._reabastecimentos = []
        self._contas_a_pagar = []
        self._quant_clientes = 0
        self._quant_funcionarios = 0
        self._quant_gerentes = 0
        self._quant_produtos = 0
        self._quant_fornecedores = 0
        self._quant_reabastecimentos = 0
        self._quant_contas_a_pagar = 0

    @property
    def clientes(self):
        return self._clientes

    @clientes.setter
    def clientes(self, clientes):
        self._clientes = clientes

    @property
    def funcionarios(self):
        return self._funcionarios

    @funcionarios.setter
    def funcionarios(self, funcionarios):
        self._funcionarios = funcionarios

    @property
    def gerentes(self):
        return self._gerentes

    @gerentes.setter
    def gerentes(self, gerentes):
        self._gerentes = gerentes

    @property
    def fornecedores(self):
        return self._fornecedores

    @fornecedores.setter
    def fornecedores(self, fornecedores):
        self._fornecedores = fornecedores

    @property
    def produtos(self):
        return self._produtos

    @produtos.setter
    def produtos(self, produtos):
        self._produtos = produtos

    @property
    def reabastecimentos(self):
        return self._reabastecimentos

    @reabastecimentos.setter
    def reabastecimentos(self, reabastecimentos):
        self._reabastecimentos = reabastecimentos

    @property
    def contas_a_pagar(self):
        return self._contas_a_pagar

    @contas_a_pagar.setter
    def contas_a_pagar(self, contas_a_pagar):
        self._contas_a_pagar = contas_a_pagar

    @property
    def quant_clientes(self):
        return self._quant_clientes

    @quant_clientes.setter
    def quant_clientes(self, quant_clientes):
        self._quant_clientes = quant_clientes

    @property
    def quant_funcionarios(self):
        return self._quant_funcionarios

    @quant_funcionarios.setter
    def quant_funcionarios(self, quant_funcionarios):
        self._quant_funcionarios = quant_funcionarios

    @property
    def quant_gerentes(self):
        return self._quant_gerentes

    @quant_gerentes.setter
    def quant_gerentes(self, quant_gerentes):
        self._quant_gerentes = quant_gerentes

    @property
    def quant_produtos(self):
        return self._quant_produtos

    @quant_produtos.setter
    def quant_produtos(self, quant_produtos):
        self._quant_produtos = quant_produtos

    @property
    def quant_fornecedores(self):
        return self._quant_fornecedores

    @quant_fornecedores.setter
    def quant_fornecedores(self, quant_fornecedores):
        self._quant_fornecedores = quant_fornecedores

    @property
    def quant_reabastecimentos(self):
        return self._quant_reabastecimentos

    @quant_reabastecimentos.setter
    def quant_reabastecimentos(self, quant_reabastecimentos):
        self._quant_reabastecimentos = quant_reabastecimentos

    @property
    def quant_contas_a_pagar(self):
        return self._quant_contas_a_pagar

    @quant_contas_a_pagar.setter
    def quant_contas_a_pagar(self, quant_contas_a_pagar):
        self._quant_contas_a_pagar = quant_contas_a_pagar

    def libera_acesso(self, cpf, senha):  # busca em funcionarios e em gerentes se existe tal cpf e senha
        if self.quant_funcionarios != 0:
            for i in range(self.quant_funcionarios):
                if self.funcionarios[i].cpf == cpf and self.funcionarios[i].senha == senha:
                    return True
        if self.quant_gerentes != 0:
            for i in range(self.quant_gerentes):
                if self.gerentes[i].cpf == cpf and self.gerentes[i].senha == senha:
                    return True

        return False

    def retorna_perfil(self, cpf, senha):  # busca em funcionarios e em gerentes e retorna esse objeto
        if self.quant_funcionarios != 0:
            for i in range(self.quant_funcionarios):
                if self.funcionarios[i].cpf == cpf and self.funcionarios[i].senha == senha:
                    return self.funcionarios[i]
        if self.quant_gerentes != 0:
            for i in range(self.quant_gerentes):
                if self.gerentes[i].cpf == cpf and self.gerentes[i].senha == senha:
                    return self.gerentes[i]

    def printa_pessoa_logada(self, pessoa_logada):  # printa algumas informacoes da pessoa
        print("Codigo usuario atual: %d" % pessoa_logada.codigo)
        print("CPF usuario atual: %s" % pessoa_logada.cpf)
        if pessoa_logada.permissao_total:  # se o atributo permissao total for true e pq a pessoa e um gerente
            print("Cargo: Gerente")
        else:
            print("Cargo: Funcionario")

    def verifica_existencia(self, valor, op):
        '''GUIA DE USO DESTA FUNCAO:
        Passe como parametro op 1 para buscar dentre os clientes
        Passe como parametro op 2 para buscar dentre os funcionarios
        Passe como parametro op 3 para buscar dentre os gerentes
        Passe como parametro op 4 para buscar dentre os produtos
        Passe como parametro op 5 para buscar dentre os fornecedores'''
        if op == 1:  # ira buscar dentre os clientes
            for i in range(self.quant_clientes):
                if self.clientes[i].cpf == valor:
                    return True
            return False
        elif op == 2:  # ira buscar dentre os funcionarios
            for i in range(self.quant_funcionarios):
                if self.funcionarios[i].cpf == valor:
                    return True
            return False
        elif op == 3:  # ira buscar dentre os gerentes
            for i in range(self.quant_gerentes):
                if self.gerentes[i].cpf == valor:
                    return True
            return False
        elif op == 4:
            for i in range(self.quant_produtos):
                if str(self.produtos[i].codigo) == str(valor):
                    return True
            return False
        elif op == 5:
            for i in range(self.quant_fornecedores):
                if self.fornecedores[i].cnpj == valor:
                    return True
            return False
        else:
            print("Operacao invalida!\n")
            return True

    def cadastra_cliente(self, pessoa_logada):
        try:
            nome = input("Insira o nome do cliente: ")
            endereco = input("Insira o endereco do cliente: ")
            telefone = input("Insira o telefone do cliente: ")
            while not telefone.isdigit():  # verifica se a string contem apenas digitos
                print("ERRO! EX telefone: 89999885533")
                telefone = input("Insira o telefone: ")
            cpf = input("Insira o CPF do cliente: ")
            while not cpf.isdigit():
                print("ERRO! EX CPF: 00723433377")
                cpf = input("Insira o CPF: ")
            rg = input("Insira o RG do cliente: ")
            while not rg.isdigit():
                print("ERRO! EX RG: 123456789")
                rg = input("Insira o RG: ")
            if not self.verifica_existencia(cpf, 1):
                self.clientes.append(Cliente(self.quant_clientes, nome, endereco, telefone, cpf, rg))  # adiciona um
                # objeto do tipo cliente a lista de cliente
                self.quant_clientes += 1
                print("\nCADASTRADO COM SUCESSO!\n")
                op = "Cadastrou Cliente de Cod: " + str(
                    self.clientes[self.quant_clientes - 1].codigo) + " e CPF: " + str(
                    self.clientes[self.quant_clientes - 1].cpf) + " em " + retorna_tempo_atual()
                pessoa_logada.historico.inserir(op)  # insere no historico da pessoa logada a operacao que ela fez
            else:
                print("\nCPF JA CADASTRADO!\n")
        except:
            print("Houve um erro!\n")

    def cadastra_funcionario(self, pessoa_logada):
        try:
            nome = input("Insira o nome: ")
            endereco = input("Insira o endereco: ")
            telefone = input("Insira o telefone: ")
            while not telefone.isdigit():
                print("ERRO! EX telefone: 89999885533")
                telefone = input("Insira o telefone: ")
            cpf = input("Insira o CPF: ")
            while not cpf.isdigit():
                print("ERRO! EX CPF: 00723433377")
                cpf = input("Insira o CPF: ")
            rg = input("Insira o RG: ")
            while not rg.isdigit():
                print("ERRO! EX RG: 123456789")
                rg = input("Insira o RG: ")
            senha = input("Insira a senha: ")
            if not self.verifica_existencia(cpf, 2):
                self.funcionarios.append(Funcionario(self.quant_funcionarios, nome, endereco, telefone, cpf, rg, senha))
                self.quant_funcionarios += 1
                print("\nCADASTRADO COM SUCESSO!\n")
                op = "Cadastrou Funcionario de Cod: " + str(
                    self.funcionarios[self.quant_funcionarios - 1].codigo) + " e CPF: " + str(
                    self.funcionarios[self.quant_funcionarios - 1].cpf) + " em " + retorna_tempo_atual()
                pessoa_logada.historico.inserir(op)
            else:
                print("\nCPF JA CADASTRADO!\n")

        except:
            print("Houve um erro!\n")

    def cadastra_gerente(self):
        try:
            nome = input("Insira o nome: ")
            endereco = input("Insira o endereco: ")
            telefone = input("Insira o telefone: ")
            while not telefone.isdigit():
                print("ERRO! EX telefone: 89999885533")
                telefone = input("Insira o telefone: ")
            cpf = input("Insira o CPF: ")
            while not cpf.isdigit():
                print("ERRO! EX CPF: 00723433377")
                cpf = input("Insira o CPF: ")
            rg = input("Insira o RG: ")
            while not rg.isdigit():
                print("ERRO! EX RG: 123456789")
                rg = input("Insira o RG: ")
            senha = input("Insira a senha: ")
            if not self.verifica_existencia(cpf, 3):
                self.gerentes.append(Gerente(self.quant_gerentes, nome, endereco, telefone, cpf, rg, senha))
                self.quant_gerentes += 1
                print("\nCADASTRADO COM SUCESSO!\n")
            else:
                print("\nCPF JA CADASTRADO!\n")
        except:
            print("\nHouve um erro!\n")

    def cadastra_produto(self, pessoa_logada):
        try:
            while 1:
                codigo = int(input("Insira o codigo do produto: "))
                if not self.verifica_existencia(codigo, 4):
                    break
                print("\nCodigo ja existente! Tente Novamente!\n")

            nome_produto = input("Insira o nome do produto: ")
            nome_produto = nome_produto.upper()
            categoria = input("Insira a categoria do produto(ex: Eletrodomestico, Higiene, Cosmeticos...): ")
            categoria = categoria.upper()
            descricao = input("Insira a descricao do produto: ")
            valor_de_venda = float(input("Insira o valor unitario de venda do produto: "))
            self.produtos.append(Produto(codigo, valor_de_venda, nome_produto, categoria, descricao))
            self.quant_produtos += 1
            print("\nCadastrado com sucesso!\n")
            op = "Cadastrou Produto de Cod: " + str(self.produtos[self.quant_produtos - 1].codigo) + " e Nome: " + str(
                self.produtos[self.quant_produtos - 1].nome_produto) + " em " + retorna_tempo_atual()
            pessoa_logada.historico.inserir(op)
        except:
            print("\nHouve um erro!\n")

    def cadastra_fornecedor(self, pessoa_logada):
        try:
            while 1:
                cnpj = input("Insira o cnpj do fornecedor: ")
                while not cnpj.isdigit():
                    print("ERRO! EX CNPJ: 82329309000194")
                    cnpj = input("Insira o CNPJ: ")
                if not self.verifica_existencia(cnpj, 5):
                    break
                print("\nCNPJ ja existente!\n")
            nome = input("Insira o nome do fornecedor: ")
            email = input("Insira o email do fornecedor: ")
            telefone = input("Insira o telefone do fornecedor: ")
            while not telefone.isdigit():
                print("ERRO! EX telefone: 89999885533")
                telefone = input("Insira o telefone: ")
            self.fornecedores.append(Fornecedor(self.quant_fornecedores, nome, cnpj, email, telefone))
            self.quant_fornecedores += 1
            op = "Cadastrou Fornecedor de Cod: " + str(
                self.fornecedores[self.quant_fornecedores - 1].codigo) + " e Nome: " + \
                 self.fornecedores[self.quant_fornecedores - 1].nome + " em " + retorna_tempo_atual()
            pessoa_logada.historico.inserir(op)
            print("\nCadastrado com sucesso!\n")
        except:
            print("\nHouve um erro!\n")

    def listar_clientes(self):
        if self.quant_clientes != 0:
            print("===============LISTANDO TODOS OS CLIENTES====================")
            for i in range(self.quant_clientes):
                print("Codigo: %d" % self.clientes[i].codigo)
                print("Nome: %s" % self.clientes[i].nome)
                print("Endereco: %s" % self.clientes[i].endereco)
                print("Telefone: %s" % self.clientes[i].telefone)
                print("CPF: %s" % self.clientes[i].cpf)
                print("RG: %s\n" % self.clientes[i].rg)
            print("\n")

    def listar_funcionarios(self):
        if self.quant_funcionarios != 0:
            print("===============LISTANDO TODOS OS FUNCIONARIOS====================")
            for i in range(self.quant_funcionarios):
                print("Codigo: %d" % self.funcionarios[i].codigo)
                print("Nome: %s" % self.funcionarios[i].nome)
                print("Endereco: %s" % self.funcionarios[i].endereco)
                print("Telefone: %s" % self.funcionarios[i].telefone)
                print("CPF: %s" % self.funcionarios[i].cpf)
                print("RG: %s\n" % self.funcionarios[i].rg)
            print("")
        else:
            print("Nenhum funcionario cadastrado!\n")

        if self.quant_gerentes != 0:
            print("===============LISTANDO TODOS OS GERENTES====================")
            for i in range(self.quant_gerentes):
                print("Codigo: %d" % self.gerentes[i].codigo)
                print("Nome: %s" % self.gerentes[i].nome)
                print("Endereco: %s" % self.gerentes[i].endereco)
                print("Telefone: %s" % self.gerentes[i].telefone)
                print("CPF: %s" % self.gerentes[i].cpf)
                print("RG: %s\n" % self.gerentes[i].rg)
            print("")
        else:
            print("Nenhum funcionario cadastrado!\n")

    def listar_produto_especifico(self):
        try:
            flag = 0
            codigo = int(input("Insira o codigo do produto: "))
            for i in range(self.quant_produtos):
                if str(self.produtos[i].codigo) == str(codigo):
                    print("Codigo: %d" % self.produtos[i].codigo)
                    print("Nome do produto: %s" % self.produtos[i].nome_produto)
                    print("Valor de compra unitario: %.2f" % self.produtos[i].valor_compra)
                    print("Valor de venda unitario: %.2f" % self.produtos[i].valor_venda)
                    print("Categoria: %s" % self.produtos[i].categoria)
                    print("Descricao: %s" % self.produtos[i].descricao)
                    print("Quantidade em estoque: %d\n" % self.produtos[i].quantidade)
                    flag = 1
                    break
            if flag == 0:
                print("\nProduto nao encontrado!\n")
        except:
            print("\nHouve um erro!\n")

    def listar_produto_por_categoria(self):
        try:
            flag = 0
            categoria = input("Insira a categoria do produto: ")
            categoria = categoria.upper()
            for i in range(self.quant_produtos):
                if self.produtos[i].categoria == categoria:
                    print("Codigo: %d" % self.produtos[i].codigo)
                    print("Nome do produto: %s" % self.produtos[i].nome_produto)
                    print("Valor de compra unitario: %.2f" % self.produtos[i].valor_compra)
                    print("Valor de venda unitario: %.2f" % self.produtos[i].valor_venda)
                    print("Descricao: %s" % self.produtos[i].descricao)
                    print("Quantidade em estoque: %d\n" % self.produtos[i].quantidade)
                    flag = 1
                    break
            if flag == 0:
                print("\nCategoria nao encontrada!\n")
        except:
            print("\nHouve um erro!\n")

    def listar_produtos(self):
        if self.quant_produtos != 0:
            print("\n===============LISTANDO TODOS OS PRODUTOS====================")
            for i in range(self.quant_produtos):
                print("Codigo: %d" % self.produtos[i].codigo)
                print("Nome do produto: %s" % self.produtos[i].nome_produto)
                print("Valor de compra unitario: %.2f" % self.produtos[i].valor_compra)
                print("Valor de venda unitario: %.2f" % self.produtos[i].valor_venda)
                print("Categoria: %s" % self.produtos[i].categoria)
                print("Descricao: %s" % self.produtos[i].descricao)
                print("Quantidade em estoque: %d\n" % self.produtos[i].quantidade)
            print("\n")
        else:
            print("\nNenhum produto cadastrado!\n")

    def listar_fornecedores(self):
        if self.quant_fornecedores != 0:
            print("\n===============LISTANDO TODOS OS FORNECEDORES====================")
            for i in range(self.quant_fornecedores):
                print("Codigo: %d" % self.fornecedores[i].codigo)
                print("Nome: %s" % self.fornecedores[i].nome)
                print("CNPJ: %s" % self.fornecedores[i].cnpj)
                print("Email: %s" % self.fornecedores[i].email)
                print("Telefone: %s\n" % self.fornecedores[i].telefone)
            print("\n")
        else:
            print("\nNenhum fornecedor cadastrado!\n")

    def listar_contas_a_pagar(self):
        if self.quant_contas_a_pagar != 0:
            print("\n===============LISTANDO TODAS AS CONTAS A PAGAR====================")
            for i in range(self.quant_contas_a_pagar):
                print("Codigo: %d" % self.contas_a_pagar[i].codigo)
                print("Codigo de Reabastecimento: %s" % self.contas_a_pagar[i].cod_reabastecimento)
                print("Valor: %.2f" % self.contas_a_pagar[i].valor)
                print("Data de pagamento: %s\n" % self.contas_a_pagar[i].data_pagamento)
            print("\n")
        else:
            print("\nNenhuma conta a pagar cadastrada!\n")

    def retorna_cliente(self, cpf):  # retorna o indice do cliente na lista, se ele nao existir retorna -1
        if self.verifica_existencia(cpf, 1):
            for i in range(self.quant_clientes):
                if self.clientes[i].cpf == cpf:
                    return i
        else:
            print("\nCliente nao encontrado\n")
            return -1

    def retorna_funcionario(self, cpf):
        if self.verifica_existencia(cpf, 2):
            for i in range(self.quant_funcionarios):
                if self.funcionarios[i].cpf == cpf:
                    return i
        else:
            print("\nFuncionario nao encontrado com esse CPF\n")
            return -1

    def retorna_gerente(self, cpf):
        if self.verifica_existencia(cpf, 3):
            for i in range(self.quant_gerentes):
                if self.gerentes[i].cpf == cpf:
                    return i
        else:
            print("\nGerente nao encontrado com esse CPF\n")
            return -1

    def retorna_produto(self, codigo):
        if self.verifica_existencia(codigo, 4):
            for i in range(self.quant_produtos):
                if str(self.produtos[i].codigo) == str(codigo):
                    return i
        else:
            print("\nProduto nao encontrado com esse Codigo\n")
            return -1

    def retorna_fornecedor(self, cnpj):
        if self.verifica_existencia(cnpj, 5):
            for i in range(self.quant_fornecedores):
                if self.fornecedores[i].cnpj == cnpj:
                    return i
        else:
            print("\nGerente nao encontrado com esse CPF\n")
            return -1

    def ver_historico_cliente(self):
        if self.quant_clientes != 0:
            try:
                cpf = input("Insira o cpf do cliente: ")
                i = self.retorna_cliente(cpf)
                if i != -1:
                    print(self.clientes[i].historico.exibir())
                    print("\n")
            except:
                print("\nHouve um erro!\n")
        else:
            print("\nNenhum Cliente cadastrado!\n")

    def ver_historico_funcionario(self):
        if self.quant_funcionarios != 0:
            try:
                cpf = input("Insira o cpf do funcionario: ")
                i = self.retorna_funcionario(cpf)
                if i != -1:
                    print(self.funcionarios[i].historico.exibir())
                    print("\n")
            except:
                print("\nHouve um erro!\n")
        else:
            print("\nNenhum funcionario cadastrado!\n")

    def ver_historico_gerente(self):
        if self.quant_gerentes != 0:
            try:
                cpf = input("Insira o cpf do gerente: ")
                i = self.retorna_gerente(cpf)
                if i != -1:
                    print(self.gerentes[i].historico.exibir())
                    print("\n")
                else:
                    print("\nNenhum Gerente encontrado com esse CPF!\n")
            except:
                print("\nHouve um erro!\n")
        else:
            print("\nNenhum gerente cadastrado!\n")

    def ver_historico_fornecedor(self):
        if self.quant_fornecedores != 0:
            try:
                cnpj = input("Insira o cnpj da fornecedora: ")
                i = self.retorna_fornecedor(cnpj)
                if i != -1:
                    print(self.fornecedores[i].historico.exibir())
                    print("\n")
            except:
                print("\nHouve um erro!\n")
        else:
            print("\nNenhum Fornecedor cadastrado!\n")

    def alterar_cadastro_cliente(self, pessoa_logada):
        if self.quant_clientes != 0:
            try:
                cpf = input("Insira o cpf do cliente: ")
                i = self.retorna_cliente(cpf)
                if i != -1:
                    nome = input("Insira o nome do cliente: ")
                    endereco = input("Insira o endereco do cliente: ")
                    telefone = input("Insira o telefone do cliente: ")
                    while not telefone.isdigit():
                        print("ERRO! EX telefone: 89999885533")
                        telefone = input("Insira o telefone: ")
                    cpf = input("Insira o CPF do cliente: ")
                    while not cpf.isdigit():
                        print("ERRO! EX CPF: 00723433377")
                        cpf = input("Insira o CPF: ")
                    rg = input("Insira o RG do cliente: ")
                    while not rg.isdigit():
                        print("ERRO! EX RG: 123456789")
                        rg = input("Insira o RG: ")
                    self.clientes[i].altera(nome, endereco, telefone, cpf, rg)
                    print("\nCadastro alterado com sucesso!\n")
                    op = "Alterou o cadastro do Cliente de Cod: " + str(self.clientes[i].codigo) + " e CPF: " \
                         + self.clientes[i].cpf + " em " + retorna_tempo_atual()
                    pessoa_logada.historico.inserir(op)
            except:
                print("\nHouve um erro!\n")
        else:
            print("\nNenhum cliente cadastrado!\n")

    def alterar_cadastro_funcionario(self, pessoa_logada):
        if self.quant_funcionarios != 0:
            try:
                cpf = input("Insira o cpf do funcionario: ")
                i = self.retorna_funcionario(cpf)
                if i != -1:
                    nome = input("Insira o nome: ")
                    endereco = input("Insira o endereco: ")
                    telefone = input("Insira o telefone: ")
                    while not telefone.isdigit():
                        print("ERRO! EX telefone: 89999885533")
                        telefone = input("Insira o telefone: ")
                    cpf = input("Insira o CPF: ")
                    while not cpf.isdigit():
                        print("ERRO! EX CPF: 00723433377")
                        cpf = input("Insira o CPF: ")
                    rg = input("Insira o RG: ")
                    while not rg.isdigit():
                        print("ERRO! EX RG: 123456789")
                        rg = input("Insira o RG: ")
                    self.funcionarios[i].altera(nome, endereco, telefone, cpf, rg)
                    print("\nCadastro alterado com sucesso!\n")
                    op = "Alterou o cadastro do Funcionario de Cod: " + str(
                        self.funcionarios[i].codigo) + " e CPF: " + \
                         self.funcionarios[i].cpf + " em " + retorna_tempo_atual()
                    pessoa_logada.historico.inserir(op)
            except:
                print("\nHouve um erro!\n")
        else:
            print("\nNenhum Funcionario cadastrado!\n")

    def alterar_cadastro_gerente(self, pessoa_logada):
        if self.quant_gerentes != 0:
            try:
                cpf = input("Insira o cpf do gerente: ")
                i = self.retorna_gerente(cpf)
                if i != -1:
                    nome = input("Insira o nome: ")
                    endereco = input("Insira o endereco: ")
                    telefone = input("Insira o telefone: ")
                    while not telefone.isdigit():
                        print("ERRO! EX telefone: 89999885533")
                        telefone = input("Insira o telefone: ")
                    cpf = input("Insira o CPF: ")
                    while not cpf.isdigit():
                        print("ERRO! EX CPF: 00723433377")
                        cpf = input("Insira o CPF: ")
                    rg = input("Insira o RG: ")
                    while not rg.isdigit():
                        print("ERRO! EX RG: 123456789")
                        rg = input("Insira o RG: ")
                    self.gerentes[i].altera(nome, endereco, telefone, cpf, rg)
                    print("\nCadastro alterado com sucesso!\n")
                    op = "Alterou o cadastro do Gerente de Cod: " + str(self.gerentes[i].codigo) + " e CPF: " \
                         + self.gerentes[i].cpf + " em " + retorna_tempo_atual()
                    pessoa_logada.historico.inserir(op)
            except:
                print("\nHouve um erro!\n")
        else:
            print("\nNenhum Gerente cadastrado!\n")

    def alterar_cadastro_produtos(self, pessoa_logada):
        if self.quant_produtos != 0:
            try:
                cod = int(input("Insira o codigo do produto: "))
                i = self.retorna_produto(cod)
                if i != -1:
                    nome_produto = input("Insira o nome do produto: ")
                    nome_produto = nome_produto.upper()
                    categoria = input("Insira a categoria do produto(ex: Eletrodomestico, Higiene, Cosmeticos...): ")
                    categoria = categoria.upper()
                    descricao = input("Insira a descricao do produto: ")
                    valor_de_compra = float(input("Insira o valor unitario de compra do produto: "))
                    valor_de_venda = float(input("Insira o valor unitario de venda do produto: "))
                    self.produtos[i].altera(valor_de_compra, valor_de_venda, nome_produto, categoria, descricao)
                    print("\nCadastro alterado com sucesso!\n")
                    op = "Alterou o cadastro do Produto de Cod: " + str(self.produtos[i].codigo) + " e Nome: " + str(
                        self.produtos[i].nome_produto) + " em " + retorna_tempo_atual()
                    pessoa_logada.historico.inserir(op)
            except:
                print("\nHouve um erro!\n")
        else:
            print("\nNenhum Produto cadastrado!\n")

    def alterar_cadastro_fornecedores(self, pessoa_logada):
        if self.quant_fornecedores != 0:
            try:
                cnpj = input("Insira o CNPJ do Fornecedor: ")
                i = self.retorna_fornecedor(cnpj)
                if i != -1:
                    nome = input("Insira o nome do fornecedor: ")
                    email = input("Insira o email do fornecedor: ")
                    telefone = input("Insira o telefone do fornecedor: ")
                    self.fornecedores[i].altera(cnpj, nome, email, telefone)
                    print("\nCadastro alterado com sucesso!\n")
                    op = "Alterou o cadastro do Fornecedor de Cod: " + str(
                        self.fornecedores[i].codigo) + " e Nome: " \
                         + self.fornecedores[i].nome + " em " + retorna_tempo_atual()
                    pessoa_logada.historico.inserir(op)
            except:
                print("\nHouve um erro!\n")
        else:
            print("\nNenhum Fornecedor cadastrado!\n")

    def reabastecer(self, pessoa_logada):
        if self.quant_produtos != 0 and self.quant_fornecedores != 0:
            try:
                codigo_produto = int(input("Insira o codigo do produto a ser reabastecido: "))
                i = self.retorna_produto(codigo_produto)
                if i != -1:
                    cnpj_fornecedor = input("Insira o CNPJ do fornecedor: ")
                    j = self.retorna_fornecedor(cnpj_fornecedor)
                    if j != -1:
                        quantidade = int(input("Insira a quantidade: "))
                        if quantidade > 0:
                            valor = float(input("Insira o valor total da compra: "))
                            if valor > 0:
                                self.reabastecimentos.append(
                                    Reabastecimento(self.quant_reabastecimentos, self.fornecedores[j].codigo,
                                                    self.produtos[i].codigo, pessoa_logada.codigo, valor, quantidade))
                                data_pagamento = retorna_daqui_a_ndias(30)
                                self.contas_a_pagar.append(
                                    Conta_a_Pagar(self.quant_contas_a_pagar, self.quant_reabastecimentos, valor,
                                                  data_pagamento))
                                self.quant_reabastecimentos += 1
                                self.quant_contas_a_pagar += 1
                                self.produtos[i].adiciona_quantidades(quantidade)
                                print("\nReabastecimento feito com sucesso!\n")
                                op = "Realizou o Reabastecimento de Cod: " + str(
                                    self.reabastecimentos[
                                        self.quant_reabastecimentos - 1].codigo) + " de Fornecedor cod: " + str(
                                    self.fornecedores[j].codigo) + " no Valor: " + str(
                                    valor) + " em " + retorna_tempo_atual()
                                pessoa_logada.historico.inserir(op)
                                op = "Realizou o Reabastecimento de Cod: " + str(
                                    self.reabastecimentos[self.quant_reabastecimentos - 1].codigo) \
                                     + " autorizado por Gerente de cod: " + str(
                                    pessoa_logada.codigo) + " Produto de cod: " + str(self.produtos[i].codigo) \
                                     + " no Valor: " + str(valor) + " em " + retorna_tempo_atual()
                                self.fornecedores[j].historico.inserir(op)
                            else:
                                print("\nA valor nao pode ser 0 ou menor\n")
                        else:
                            print("\nA quantidade nao pode ser 0 ou menor\n")
            except:
                print("\nHouve um erro!\n")
        else:
            print("\nNenhum Produto, Fornecedor ou Gerente cadastrado!\n")

    def remover_cliente(self, pessoa_logada):
        if self.quant_clientes != 0:
            try:
                cpf = input("Insira o cpf do cliente: ")
                i = self.retorna_cliente(cpf)
                if i != -1:
                    op = "Removeu Cliente de cod: " + str(self.clientes[i].codigo) + " CPF: " + \
                         self.clientes[i].cpf + " em " + retorna_tempo_atual()
                    self.clientes.pop(i)  # retira o cliente da lista por meio do indice retornado
                    self.quant_clientes -= 1
                    print("\nREMOVIDO COM SUCESSO!\n")
                    pessoa_logada.historico.inserir(op)
                else:
                    print("\nNenhum Cliente encontrado com esse CPF!\n")
            except:
                print("\nOcorreu um erro!\n")
        else:
            print("\nNenhum cliente cadastrado!\n")

    def remover_funcionario(self, pessoa_logada):
        if self.quant_funcionarios != 0:
            try:
                cpf = input("Insira o cpf do funcionario: ")
                i = self.retorna_funcionario(cpf)
                if i != -1:
                    op = "Removeu Funcionario de cod: " + str(self.funcionarios[i].codigo) \
                         + " CPF: " + self.funcionarios[i].cpf + " em " + retorna_tempo_atual()
                    self.funcionarios.pop(i)
                    self.quant_funcionarios -= 1
                    print("\nREMOVIDO COM SUCESSO!\n")
                    pessoa_logada.historico.inserir(op)
                else:
                    print("\nNenhum Funcionario encontrado com esse CPF!\n")
            except:
                print("\nOcorreu um erro!\n")
        else:
            print("\nNenhum Funcionario cadastrado!\n")

    def remover_gerente(self, pessoa_logada):
        if self.quant_gerentes != 0:
            try:
                cpf = input("Insira o cpf do gerente: ")
                i = self.retorna_gerente(cpf)
                if i != -1:
                    op = "Removeu Gerente de cod: " + str(self.gerentes[i].codigo) \
                         + " CPF: " + self.gerentes[i].cpf + " em " + retorna_tempo_atual()
                    self.gerentes.pop(i)
                    self.quant_gerentes -= 1
                    print("\nREMOVIDO COM SUCESSO!\n")
                    pessoa_logada.historico.inserir(op)
                else:
                    print("\nNenhum Gerente encontrado com esse CPF!\n")
            except:
                print("\nOcorreu um erro!\n")
        else:
            print("\nNenhum Gerente cadastrado!\n")

    def remover_produto(self, pessoa_logada):
        if self.quant_produtos != 0:
            try:
                codigo = int(input("Insira o codigo do produto: "))
                i = self.retorna_produto(codigo)
                if i != -1:
                    op = "Removeu Produto de cod: " + str(self.produtos[i].codigo) + " em " + retorna_tempo_atual()
                    self.produtos.pop(i)
                    self.quant_produtos -= 1
                    pessoa_logada.historico.inserir(op)
                    print("\nREMOVIDO COM SUCESSO!\n")
                else:
                    print("\nNenhum Produto encontrado com esse CPF!\n")
            except:
                print("\nOcorreu um erro!\n")
        else:
            print("\nNenhum Produto cadastrado!\n")

    def remover_fornecedor(self, pessoa_logada):
        if self.quant_fornecedores != 0:
            try:
                cnpj = input("Insira o cnpj do fornecedor: ")
                i = self.retorna_fornecedor(cnpj)
                if i != -1:
                    op = "Removeu Fornecedor de cod: " + str(self.fornecedores[i].codigo) \
                         + " CNPJ: " + self.fornecedores[i].cnpj + " em " + retorna_tempo_atual()
                    self.fornecedores.pop(i)
                    self.quant_fornecedores -= 1
                    pessoa_logada.historico.inserir(op)
                    print("\nREMOVIDO COM SUCESSO!\n")
                else:
                    print("\nNenhum Fornecedor encontrado com esse CPF!\n")
            except:
                print("\nOcorreu um erro!\n")
        else:
            print("\nNenhum Fornecedor cadastrado!\n")
