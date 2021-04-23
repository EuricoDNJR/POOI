from ClassSistema import *
from ClassFuncionario_Gerente import Gerente
sys = Sistema()
primeiro_acesso = True
while 1:
    if primeiro_acesso:  # verificando se e o primeiro acesso
        print("OlA, SEJA BEM-VINDO AO SISTEMA!!\n")
        print("Como e o primeiro acesso, obrigatoriamente devera cadastrar um gerente!!\n")
        print("Simples e rapido!!\n")
        while sys.quant_gerentes == 0:  # verificando se deu certo cadastrar o gerente, por meio da quantidade
            sys.cadastra_gerente()  # cadastra o gerente

        primeiro_acesso = False  # se deu tudo certo, nao ira ter mais primeiro acesso
    else:
        try:
            print("========PAINEL DE ACESSO==========")
            login = input("Insira seu CPF: ")
            senha = input("Insira sua Senha: ")
            print("==================================")
            if sys.libera_acesso(login, senha):  # libera acesso por meio do cpf e senha
                print("\nLOGADO!\n")
                pessoa_logada = sys.retorna_perfil(login, senha)  # atribui a variavel o objeto da pessoa logada
                while 1:
                    sys.printa_pessoa_logada(pessoa_logada)  # printa algumas informacoes da pessoa logada
                    print("Data e hora atual: " + retorna_tempo_atual())
                    print("1 - Cadastrar\n"
                          "2 - Listar\n"
                          "3 - Historico\n"
                          "4 - Alterar\n"
                          "5 - Reabastecer(Disponivel apenas para Gerentes!)\n"
                          "6 - Excluir\n"
                          "Qualquer outra tecla para Logout\n")
                    try:
                        op = int(input())
                        if op == 1:
                            print("1 - Cadastrar Cliente\n"
                                  "2 - Cadastrar Funcionario(Disponivel apenas para Gerentes!)\n"
                                  "3 - Cadastrar Produto\n"
                                  "4 - Cadastrar Fornecedor(Disponivel apenas para Gerentes!)\n"
                                  "5 - Cadastrar Gerente(Disponivel apenas para Gerentes!)\n"
                                  "Qualquer outra tecla para Voltar\n")
                            try:
                                op = int(input())
                                if op == 1:
                                    sys.cadastra_cliente(pessoa_logada)
                                elif op == 2 and isinstance(pessoa_logada, Gerente): # verifica a opcao e se a pessoa e
                                    # uma instancia de Gerente
                                    sys.cadastra_funcionario(pessoa_logada)
                                elif op == 3:
                                    sys.cadastra_produto(pessoa_logada)
                                elif op == 4 and isinstance(pessoa_logada, Gerente):
                                    sys.cadastra_fornecedor(pessoa_logada)
                                elif op == 5 and isinstance(pessoa_logada, Gerente):
                                    sys.cadastra_gerente()
                                else:
                                    pass
                            except:
                                pass

                        elif op == 2:
                            print("1 - Listar todos os Clientes\n"
                                  "2 - Listar todos os Funcionarios e Gerentes(Disponivel apenas para Gerentes!)\n"
                                  "3 - Listar todos os Produtos\n"
                                  "4 - Listar um Produto Especifico\n"
                                  "5 - Listar Produto por Categoria\n"
                                  "6 - Listar todos os Fornecedores(Disponivel apenas para Gerentes!)\n"
                                  "7 - Listar todas as Contas a Pagar(Disponivel apenas para Gerentes!)\n"
                                  "Qualquer outra tecla para Voltar\n")
                            try:
                                op = int(input())
                                if op == 1:
                                    sys.listar_clientes()
                                elif op == 2 and isinstance(pessoa_logada, Gerente):
                                    sys.listar_funcionarios()
                                elif op == 3:
                                    sys.listar_produtos()
                                elif op == 4:
                                    sys.listar_produto_especifico()
                                elif op == 5:
                                    sys.listar_produto_por_categoria()
                                elif op == 6 and isinstance(pessoa_logada, Gerente):
                                    sys.listar_fornecedores()
                                elif op == 7 and isinstance(pessoa_logada, Gerente):
                                    sys.listar_contas_a_pagar()
                                else:
                                    pass
                            except:
                                pass

                        elif op == 3:
                            print("1 - Exibir historico de um Cliente\n"
                                  "2 - Exibir historico de um Funcionario(Disponivel apenas para Gerentes!)\n"
                                  "3 - Exibir historico de um Gerente(Disponivel apenas para Gerentes!)\n"
                                  "4 - Exibir historico de um Fornecedor(Disponivel apenas para Gerentes!)\n"
                                  "Qualquer outra tecla para Voltar\n")
                            try:
                                op = int(input())
                                if op == 1:
                                    sys.ver_historico_cliente()
                                elif op == 2 and isinstance(pessoa_logada, Gerente):
                                    sys.ver_historico_funcionario()
                                elif op == 3 and isinstance(pessoa_logada, Gerente):
                                    sys.ver_historico_gerente()
                                elif op == 4 and isinstance(pessoa_logada, Gerente):
                                    sys.ver_historico_fornecedor()
                                else:
                                    pass
                            except:
                                pass
                        elif op == 4:
                            print("1 - Alterar cadastro Cliente\n"
                                  "2 - Alterar cadastro Funcionario(Disponivel apenas para Gerentes!)\n"
                                  "3 - Alterar cadastro Gerente(Disponivel apenas para Gerentes!)\n"
                                  "4 - Alterar cadastro Fornecedor(Disponivel apenas para Gerentes!)\n"
                                  "5 - Alterar cadastro Produto\n"
                                  "Qualquer outra tecla para Voltar\n")
                            try:
                                op = int(input())
                                if op == 1:
                                    sys.alterar_cadastro_cliente(pessoa_logada)
                                elif op == 2 and isinstance(pessoa_logada, Gerente):
                                    sys.alterar_cadastro_funcionario(pessoa_logada)
                                elif op == 3 and isinstance(pessoa_logada, Gerente):
                                    sys.alterar_cadastro_gerente(pessoa_logada)
                                elif op == 4 and isinstance(pessoa_logada, Gerente):
                                    sys.alterar_cadastro_fornecedores(pessoa_logada)
                                elif op == 5:
                                    sys.alterar_cadastro_produtos(pessoa_logada)
                                else:
                                    pass
                            except:
                                pass
                        elif op == 5 and isinstance(pessoa_logada, Gerente):
                            sys.reabastecer(pessoa_logada)
                        elif op == 6:
                            print("1 - Remover Cliente\n"
                                  "2 - Remover Funcionario(Disponivel apenas para Gerentes!)\n"
                                  "3 - Remover Gerente(Disponivel apenas para Gerentes!)\n"
                                  "4 - Remover Fornecedor(Disponivel apenas para Gerentes!)\n"
                                  "5 - Remover Produto\n"
                                  "Qualquer outra tecla para Voltar\n")
                            try:
                                op = int(input())
                                if op == 1:
                                    sys.remover_cliente(pessoa_logada)
                                elif op == 2 and isinstance(pessoa_logada, Gerente):
                                    sys.remover_funcionario(pessoa_logada)
                                elif op == 3 and isinstance(pessoa_logada, Gerente):
                                    sys.remover_gerente(pessoa_logada)
                                elif op == 4 and isinstance(pessoa_logada, Gerente):
                                    sys.remover_fornecedor(pessoa_logada)
                                elif op == 5:
                                    sys.remover_produto(pessoa_logada)
                                else:
                                    pass
                            except:
                                pass
                        else:
                            print("\nDESLOGADO COM SUCESSO!\n")
                            break
                    except:
                        print("\nDESLOGADO COM SUCESSO!\n")
                        break
            else:
                print("\nCPF OU SENHA INCORRETOS! TENTE NOVAMENTE!\n")
        except:
            print("\nHouve um erro!\n")