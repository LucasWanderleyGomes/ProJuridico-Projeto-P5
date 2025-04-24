# language: pt
Funcionalidade: Gerenciamento de Mensagens de Suporte

  Cenário: Enviar mensagem de suporte
    Dado que a API de suporte está disponível
    Quando eu envio uma mensagem de suporte com:
      | nome     | email            | mensagem           |
      | "Maria"  | "maria@email.com" | "Preciso de ajuda" |
    