# Sistema Simples de Gerenciamento de Comércio

Esse é um sistema de gerenciamento para comércios, implementado em Python. O programa tem como objetivo gerenciar a entrada e saída de clientes, o controle de estoque e o gerenciamento de funcionários, gerentes e fornecedores.
## Como utilizar

O programa é implementado por meio de classes e métodos em Python. Para utilizar o sistema, deve-se executar o arquivo 

    main.py

Ao executar o programa, será solicitado o cadastro de um gerente, caso seja o primeiro acesso. Em seguida, o usuário deverá inserir o CPF e a senha para acessar o sistema.

O sistema permite a realização de diversas operações, como o cadastro de clientes, funcionários, produtos e fornecedores, além da listagem desses itens. Também é possível realizar operações de alteração e exclusão de itens, além de reabastecimento de estoque (disponível apenas para gerentes).

O sistema também permite a visualização do histórico de clientes, funcionários, gerentes e fornecedores.
## Dependências

Esse programa não possui dependências externas.
## Funcionamento

- O programa utiliza as classes ```Sistema```, ```Pessoa```, ```Cliente```, ```Funcionario```, ```Gerente```, ```Produto```, ```Fornecedor```, ```ContaPagar``` e ```Historico```. Cada classe é responsável por controlar determinados aspectos do sistema, como o controle de estoque, o histórico de operações realizadas e o acesso ao sistema.

- O programa utiliza o padrão de projeto Singleton para garantir que apenas uma instância da classe Sistema seja criada durante a execução do programa.

- As operações de cadastro, alteração e exclusão de itens são realizadas por meio de métodos específicos de cada classe.


Esse sistema foi desenvolvido como projeto final para a disciplina de Programação Orientada a Objetos I. 

Obs: O diagrama de todo o sistema está na pasta *diagrama*.
