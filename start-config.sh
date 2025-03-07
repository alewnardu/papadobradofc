# Executando comandos dentro do container da aplicação
echo "🔄 Configurando ambiente do Flask..."
docker exec -it papadobradofc_app bash -c "
    export FLASK_APP='app.app:app' &&
    export FLASK_ENV='development' &&
    export SECRET_KEY='9870e1457b4e12f21224f6c4354f41ff9cfea58070414c8b' &&
    env | grep FLASK
"

# Criando o usuário do banco de dados
echo "👤 Criando usuário do banco de dados..."
docker exec -it papadobradofc_db bash -c "
    mysql -uroot -p\${MYSQL_ROOT_PASSWORD} -e \"
        CREATE USER IF NOT EXISTS 'papadobradofc'@'%' IDENTIFIED BY 'Senh4ppfc';
        GRANT ALL PRIVILEGES ON papadobradofc.* TO 'papadobradofc'@'%';
        FLUSH PRIVILEGES;
    \"
"

# Rodando as migrações
echo "📜 Executando migrações do banco..."
docker exec -it papadobradofc_app bash -c "
    flask db init && 
    flask db migrate -m 'Criando tabelas iniciais' &&
    flask db upgrade
"
