# Projuridico

**Projuridico** é uma plataforma voltada para a comunidade de mulheres empreendedoras, oferecendo um espaço seguro e colaborativo para networking, aprendizado e acesso a eventos. O site também apresenta um escritório de advocacia especializado em atender as necessidades jurídicas desse público.

## 📌 Funcionalidades

- **Landing Page**: Apresentação do espaço de advocacia e da proposta do projeto.
- **Área de Login**: Acesso restrito à comunidade.
- **Comunidade**:
  - Visualização de eventos.
  - Envio de mensagens entre usuárias.

## 🎨 Tecnologias Utilizadas

- **Front-end**: React
- **Back-end**: Django, Django Rest Framework
- **Banco de Dados**: PostgreSQL / Mysql
- **Autenticação**: JWT
- **Hospedagem**: A decidir

## 🚀 Como Executar o Projeto

### 🔧 Pré-requisitos

Certifique-se de ter instalado:
- [Node.js](https://nodejs.org/)
- [Python 3.10+](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/) 
- [MySQL](https://www.mysql.com/)


### 📥 Clonar o repositório
```bash
git clone https://github.com/seu-usuario/projuridico.git
cd projuridico
```

### 🔥 Back-end
```bash
cd backend
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 🎨 Front-end
```bash
cd frontend
npm install
npm run dev
```

## 📄 Licença

Este projeto é de código fechado e não está disponível para distribuição pública.



