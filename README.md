# 🎬 Flix API

A **Flix API** é uma aplicação backend desenvolvida com **Django** e **Django REST Framework**, projetada para gerenciar uma plataforma de streaming de filmes e séries.

---

## 🚀 Funcionalidades

- Cadastro e autenticação de usuários (CRUD completo: create, read, update, delete)
- Listagem de filmes e séries (Endpoints get para leitura)
- Detalhes de cada título (Detail views)
- Avaliações e comentários de usuários (App django de reviews para os filmes)

---

## 🛠️ Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [SQLite](https://www.sqlite.org/) (padrão, pode ser substituído por outro banco de dados)

---

## 📦 Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/victorgoveia/flix-api.git
   cd flix-api
   ```

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Aplique as migrações:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

---

## 🔑 Autenticação

A API utiliza autenticação baseada em tokens. Para obter um token:

1. Crie um usuário:

   ```bash
   python manage.py createsuperuser
   ```

2. Obtenha o token:

   Envie uma requisição POST para `/api/authentication/token/` com as credenciais:

   ```json
   {
     "username": "seu_usuario",
     "password": "sua_senha"
   }
   ```

   A resposta conterá o token de acesso.

    ```json
   {
     "refresh": "token_refresh",
     "access": "token_access"
   }
   ```

---

## 📁 Estrutura do Projeto

```
flix-api/
├── app/                     # Configurações principais do Django (settings, urls, wsgi)
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── authentication/          # App de autenticação (JWT, criação de usuários, login)
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── ...
├── genres/                  # App para gerenciamento de gêneros de filmes/séries
│   └── ...
├── movies/                  # App para gerenciamento de filmes e séries
│   └── ...
├── reviews/                 # App para comentários e avaliações
│   └── ...
├── actors/                  # App para gerenciamento de atores
│   └── ...
├── manage.py                # Gerenciador padrão do Django
├── requirements.txt         # Lista de dependências do projeto
└── README.md                # Documentação do projeto
```

---

## 📞 Contato

Desenvolvido por [Victor Goveia](https://github.com/victorgoveia).
