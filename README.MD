# Descrição do Projeto:
Ester README tem por objetivo fornecer as informações necessárias para utilização desta api Rest que simula o sistema de.
jogos da Mega-Sena.


#  🏗 Ferramentas do Projeto :
 - Design pattern - MVC
 - ORM - Flask_SQLAlchemy
 - Autenticação e Segurança - Flask JWT extended
 - Gerenciamento das Rotas - Flask Restful
 - Serialização - Flask Marshmallow
 - WebCrawler - Selenium, GeckoDriverManager, bs4
 - Gerenciador de alterações do banco - flask_migrate


# 🚨 Requisitos
- Banco de dados PostgresSQL:
- Poetry para gerenciar os pacotes e instalar as dependências
- configurar o .Env a partir do .Env.Example para se conectar com o Banco e definir a senha de criptografia do JWT
- startar as migrates para construção das tabelas do banco de dados
- startar o servidor.


# 🏗  REST API

Api Restful com CRUD do usuário, Autenticação de rotas, e criação de Jogos Simulados na Mega-Sena  
## USER

## Pegar os dados do seu usuário

### Request
`GET /user`

    curl -i -H 'Authorization: Bearer <TOKEN>' http://localhost:5000/user

### Response

    {
        "msg": "success",
        "data": {
            "id": "1",
            "profile_picture": "http://picsum.photo/200/200",
            "email": "user@gmail.com",
            "name": "new_name",
            "phone": "66666666"
        }
    }


## Criando um novo usuário
### Request
`POST /user`

    curl -i -H 'Accept: application/json' -d 'name=username&phone=999999&email=youremail@gmail.com&profile_picture=http://link&password=your_password,' http://localhost:5000/user

### Response

    HTTP/1.1 200 OK
    msg: success
    data:
      "id": "your_id"
      "name": "username",
      "phone": "999999",
      "email": "seu_email@gmail.com",
      "profile_picture": "http://picsum.photo/200/200",
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2


## Fazendo loggin com seu usuário
### Request
`POST /signin`

    curl -i -H 'Accept: application/json' -d 'email=user@email.com&password=user_password' http://localhost:5000/signin

### Response

    HTTP/1.1 200 OK
    {
      "msg": "created",
      "data": {
        "phone": "66666666",
        "email": "henriqueafcarvalho@gmail.com",
        "profile_picture": "http://picsum.photo/200/200",
        "id": "1",
        "name": "new_name"
      },
      "access_token": "<TOKEN>"
    }
    Status: 200 OK
    Connection: close
    Content-Type: application/json
    Content-Length: 2
    

## Atualizando dados do seu usuário
### Request
`PATCH /user`

    curl -i -H 'Authorization: Bearer <TOKEN>' -X PATCH -d 'name=new_name&phone=999999' http://localhost:5000/user

### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 228
    Server: Werkzeug/1.0.1 Python/3.9.1
    Date: Fri, 16 Apr 2021 02:21:25 GMT
    
    {
        "msg": "success",
        "data": {
            "phone": "9999999",
            "email": "henriqueafcarvalho@gmail.com",
            "profile_picture": "http://picsum.photo/200/200",
            "id": "1",
            "name": "new_name"
        }
    }


## Deletar seu usuário
### Request
`DELETE /user`

    curl -X DELETE 'http://localhost:5000/user ' -H 'Authorization: Bearer <TOKEN>'

### Response

    {
        "msg": "user X has been deleted"
    }


## GAME

## Criar um novo jogo na mega sena , tendo no retorno a data de criação, o resultado do jogo feito, e os números que você acertou:
### Request
`POST /game`

    curl -i -H 'Authorization: Bearer <TOKEN>' -d 'sort_numbers=number_in_range_6_to_10' http://localhost:5000/user

### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 413
    Server: Werkzeug/1.0.1 Python/3.9.1
    Date: Fri, 3 Apr 2021 00:00:13 GMT
    
    {
        "data": {
            "correct_numbers": "you didn't hit any numbers",
            "id": "number",
            "create_at": "0000-00-00 00:00:00.0000",
            "mega_result": "3, 20, 22, 32, 35, 50",
            "user_id": 1,
            "sorted_numbers": "12, 1, 25, 51, 21, 11",
            "sort_numbers": "6",
            "result_sort": "N\u00e3o foi dessa vez, voc\u00ea n\u00e3o foi sorteado, por favor, tente novamente!."
        }
    }


## listar todos os resultados de sorteios do usuário logado:
### Request
`GET /game`

    curl -i -H 'Authorization: Bearer <TOKEN>' http://localhost:5000/games

### Response

    HTTP/1.0 200 OK
    Content-Type: application/json
    Content-Length: 9894
    Server: Werkzeug/1.0.1 Python/3.9.1
    Date: Fri, 13 Apr 2021 00:00:00 GMT

    {
        "data": [
            {
                "correct_numbers": "35, 50",
                "id": "1",
                "create_at": "0000-00-00 00:00:00.0000",
                "mega_result": "'03', '20', '22', '32', '35', '50'",
                "user_id": 1,
                "sorted_numbers": "28, 46, 22, 50, 48, 29, 35",
                "sort_numbers": "7",
                "result_sort": "loser"
            },
            {
                "correct_numbers": "3",
                "id": "2",
                "create_at": "0000-00-00 00:00:00.0000",
                "mega_result": "'3', '20', '22', '32', '35', '50'",
                "user_id": 1,
                "sorted_numbers": "3, 34, 49, 39, 36, 21",
                "sort_numbers": "6",
                "result_sort": "loser"
            }
       ]
    }