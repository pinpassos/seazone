# seazone
back-end to seazone.

## Instalação
No diretório raiz do projeto podemos encontrar o arquivo requirements.txt onde se encontram as dependências necessárias para o funcionamento correto da aplicação.<br>
Para instalar as dependências, primeiro rodamos o seguinte comando para criar um ambiente virtual própio para o projeto:<br>
Utilizando a versão do Python <b>^3.10.6</b>, execute:
```bash
pip install virtualenv <nome_da_virtualenv>
```
Para acessar sua virtualenv:
- Linux: source <nome_da_virtualenv>/bin/activate
- Windows: <nome_da_virtualenv>\Scripts\Activate.ps1
<br>
Após estarmos com virtualenv ativada, precisamos instalar as dependências dentro dela rodando o seguinte comando no diretório onde se encontra o arquivo requirements.txt

```bash
pip install -r requirements.txt
```
### PostgreSQL
Utilizando a versão <b>^15.3</b> devemos criar um banco de dados para o projeto utilizando o comando:<br>
```bash
CREATE DATABASE seazone;
```
Após o banco estar criado precisamos criar um usuário e garantir o acesso ao banco:<br>
```bash
CREATE USER seazone_user WITH PASSWORD 'seazone_password';
GRANT ALL PRIVILEGES ON DATABASE seazone TO seazone_user;
ALTER ROLE "seazone_user" WITH LOGIN;
```
## Fixtures
Dentro do diretório "fixtures" podemos encontrar nossos seeders, conténdo dados para as bases de Property, Announcement e Booking.<br>
Para popular nosso banco podemos rodar o comando:
```bash
python3 manage.py loaddata properties_fixtures.json announcements_fixtures.json bookings_fixtures.json
```
## Testes
Para rodar os testes do projeto basta rodar o comando:
```bash
python3 manage.py test
```

## Property endpoint
- Allowed methods: ['get', 'post', 'delete', 'put', 'patch', 'head', 'options']
- Payload: {
            "code": str,
            "number_of_guests": int,
            "number_of_bathrooms": int,
            "allowed_pet": bool,
            "cleaning_cost": float,
            "activation_date": date
        }
- List: http://127.0.0.1:8000/seazone/api/properties/
- Retrieve: http://127.0.0.1:8000/seazone/api/properties/<int:id>
- Post: http://127.0.0.1:8000/seazone/api/properties/
- Update: http://127.0.0.1:8000/seazone/api/properties/<int:id>
- Delete: http://127.0.0.1:8000/seazone/api/properties/<int:id>

## Announcement endpoint
- Allowed methods: ['get', 'post', 'head', 'put', 'patch', 'options']
- Payload: {
            "property": {
                "code": ste,
                "number_of_guests": int,
                "number_of_bathrooms": int,
                "allowed_pet": bool,
                "cleaning_cost": float,
                "activation_date": date
            },
            "plataform_name": str,
            "plataform_rate": float
        }
- List: http://127.0.0.1:8000/seazone/api/announcements/
- Retrieve: http://127.0.0.1:8000/seazone/api/announcements/<int:id>
- Post: http://127.0.0.1:8000/seazone/api/announcements/
- Update: http://127.0.0.1:8000/seazone/api/announcements/<int:id>
  
## Booking endpoint
- Allowed methods: ['get', 'post', 'delete', 'head', 'options']
- Payload: {
            "announcement": {
                "property": {
                    "code": str,
                    "number_of_guests": int,
                    "number_of_bathrooms": int,
                    "allowed_pet": bool,
                    "cleaning_cost": float,
                    "activation_date": date
                },
                "plataform_name": str,
                "plataform_rate": float
            },
            "check_in": date,
            "check_out": date,
            "number_of_guests": int,
            "comment": "Booking for test"
        }
- List: http://127.0.0.1:8000/seazone/api/bookings/
- Retrieve: http://127.0.0.1:8000/seazone/api/bookings/<int:id>
- Post: http://127.0.0.1:8000/seazone/api/bookings/
- Delete: http://127.0.0.1:8000/seazone/api/bookings/<int:id>
