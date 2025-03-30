# language: pt
Funcionalidade: Obter token de autenticação

  Cenário: Obter token com credenciais válidas
    Dado que eu tenho credenciais válidas
    Quando eu solicito um token
    Então o sistema deve retornar um token válido

  Cenário: Falha ao obter token com credenciais inválidas
    Dado que eu tenho credenciais inválidas
    Quando eu solicito um token
    Então o sistema deve retornar um erro de autenticação