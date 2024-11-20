# Social-Midia-API

### API 

## Tecnologias(Backend)
- Pytho3.11
- PostgreSql
- Django
- JWT
- Postman

## FUNCIONALIDADES

- Registro e Cadastro de usuários
- Autenticação e autorização usando JWTs
- CRUD(Postagens)
- CRUD(Comentários)
- Likes(Nas Postagens)

## Configuração do ambiente
Siga as etapas abaixo para configurar o ambiente de desenvolvimento
1. Certifique-se de ter o python instalado. Recomenda-se utilizar a versão 3.11 ou superior
2. Clone este repositório para o seu ambiente local

  ```shell
    git clone https://github.com/corteisjr/Social-midia-API.git
  ```
3. Acesse o diretório do projeto
     ```shell
      cd Social-midia-API
     ```
4. Crie um ambiente virtual para isolar as dependências do projeto:
    ```shell
      python -m venv venv
    ```

5. Ative o ambiente virtual:

   - No Windows:

     ```shell
     venv\Scripts\activate
     ```

   - No Linux ou macOS:

     ```shell
     source venv/bin/activate
     ```

6. Instale as dependências do projeto:

   ```shell
   pip install -r requirements.txt
   ```
7. Configure a base de dados Postgres(Lembre-se de ter o PSQL instalado na sua máquina)
  Para usuários linux
   ```shell
     sudo su postgres
   ```
   De seguida, pqsl

   Crie a a base de dados
      ```shell
         CREATE DATABASE coredb;
      ```
   Para conectar a base de dados, é necessário ter um USER com a Senha
         ```shell
             CREATE USER core WITH PASSWORD 'suasenha';
          ```
   Garantir acesso a base de dados
     ```shell
       GRANT ALL PRIVILEGES ON DATABASE coredb TO core;
     ```
8. Instale as dependências do projeto
      ```shell
         pip install -r requirements.txt
      ```
9. Adicione um arquivo .env
     ```shell
          SECRET_KEY = '...'
          DB_NAME = '...'
          DB_USER = '...'
          DB_PASSWORD = '...'
          DB_PORT = '...'
     ```

10.  Execute as migrações do banco de dados:

   ```shell
     python manage.py migrate
   ```
11. Inicie o servidor de desenvolvimento:

   ```shell
     python manage.py runserver
   ```
   
   
   











