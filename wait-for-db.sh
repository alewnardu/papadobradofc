#!/bin/sh
echo "Aguardando MySQL subir completamente em $DB_HOST..."

while ! nc -z "$DB_HOST" 3306; do
    sleep 2
done

echo "Banco de dados está pronto! Iniciando a aplicação..."
exec "$@"
