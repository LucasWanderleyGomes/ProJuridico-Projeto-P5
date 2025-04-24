# language: pt
Funcionalidade: Gerenciamento de Processos Jurídicos

  Cenário: Criar um novo processo válido
    Dado que o endpoint de processos está disponível
    Quando eu envio os dados de um novo processo:
      | campo      | valor               |
      | categoria  | "Trabalhista"       |
      | titulo     | "Processo trabalhista" |
      | descricao  | "Descrição do caso" |
    Então o sistema deve retornar status 201
    E o processo deve ser criado no banco de dados

  Cenário: Tentar criar processo sem dados obrigatórios
    Dado que o endpoint de processos está disponível
    Quando eu envio os dados de um novo processo:
      | campo      | valor               |
      | categoria  | ""                  |
      | titulo     | ""                  |
    Então o sistema deve retornar status 400