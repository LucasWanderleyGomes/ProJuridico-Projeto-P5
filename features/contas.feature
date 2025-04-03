# language: pt
Funcionalidade: Cadastro de Usuários (Signup)

  Cenário: Cadastrar usuário comum com dados válidos
    Dado que eu tenho os seguintes dados válidos:
      | email             | username      | password |
      | novo@teste.com     | usuario_novo  | senha123 |
    Quando eu envio uma requisição POST para "/api/v2/signup/"
    Então o sistema deve retornar status 201
    E o usuário deve ser criado no banco com os campos:
      | email             | username      |
      | novo@teste.com     | usuario_novo  |

  Cenário: Falha ao cadastrar com email duplicado
    Dado que já existe um usuário com email "duplicado@teste.com"
    Quando eu tento cadastrar com o mesmo email:
      | email             | username      | password |
      | duplicado@teste.com | usuario_dup  | senha123 |
    Então o sistema deve retornar status 400
    E a resposta deve conter a mensagem "Já existe um usuário com este email"

  Cenário: Cadastrar superusuário (via flag)
    Dado que eu tenho os seguintes dados de superusuário:
      | email             | username      | password | is_superuser | is_staff |
      | admin@teste.com    | admin_user    | senha123 | True         | True     |
    Quando eu envio uma requisição POST para "/api/v2/signup/"
    Então o sistema deve retornar status 201
    E o usuário deve ter "is_superuser" e "is_staff" como True