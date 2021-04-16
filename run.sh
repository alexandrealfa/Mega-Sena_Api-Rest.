#!/bin/bash

virtualenv venv &&
source venv/bin/activate &&
pip install --require-hashes -r requirements.txt &&
echo "Digite o seu usuário do postgres =) : " &&
read user_name  &&
echo "Digite sua senha do usuário do postgres =) :" &&
read password &&
echo "Digite um nome para o seu novo banco de dados :) :" &&
read db_name &&
echo -e "FLASK_APP=app\n">.env &&
echo -e "FLASK_ENV=development\n">>.env &&
echo -e "FLASK_RUN_PORT=5000\n">>.env &&
echo -e "FLASK_DB_URI=postgresql://$user_name:$password@localhost:5432/$db_name\n">>.env &&
echo "SECRET_KEY=$(openssl rand -base64 32)">>.env &&
source .env &&
flask db upgrade &&
flask run