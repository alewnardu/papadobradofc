#!/bin/bash

# Definindo variáveis de ambiente
export SECRET_KEY="9870e1457b4e12f21224f6c4354f41ff9cfea58070414c8b"
export DB_USERNAME="papadobradofc"
export DB_PASSWORD="Senh4ppfc"
export DB_HOST="papadobradofc.mysql.pythonanywhere-services.com"
export DB_NAME="papadobradofc$papadobradofc"

# Verificando se as variáveis foram definidas corretamente
echo "Variáveis de ambiente definidas:"
echo "SECRET_KEY=$SECRET_KEY"
echo "DB_USERNAME=$DB_USERNAME"
echo "DB_PASSWORD=$DB_PASSWORD"
echo "DB_HOST=$DB_HOST"
echo "DB_NAME=$DB_NAME"