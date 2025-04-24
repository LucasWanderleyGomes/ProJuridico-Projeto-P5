# language: pt
Funcionalidade: Gerenciamento de Consultas Jurídicas

  Cenário: Criar uma nova consulta válida
    Dado que o endpoint de consultas está disponível
    Quando eu envio os dados de uma nova consulta:
      | campo           | valor                  |
      | nome_cliente    | "João Silva"           |
      | numero_processo | "123456789"            |
      | assunto         | "Divórcio consensual"  |
      | descricao       | "Orientação sobre partilha de bens" |
    Então o sistema deve retornar status 201
    E a consulta deve ser criada no banco de dados

  Cenário: Tentar criar consulta sem dados obrigatórios
    Dado que o endpoint de consultas está disponível
    Quando eu envio os dados de uma nova consulta:
      | campo           | valor  |
      | nome_cliente    | ""     |
      | numero_processo | ""     |
    Então o sistema deve retornar status 400