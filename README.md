# papadobradofc

Repositório destinado ao projeto inicial de controle de peladas de futebol.

# Declaração de variáveis de ambiente

docker exec -it papadobradofc_app bash
export FLASK_APP="app.app:app"
export FLASK_ENV="development"
export SECRET_KEY="9870e1457b4e12f21224f6c4354f41ff9cfea58070414c8b"
export FLASK_DEBUG=1
env | grep FLASK

# Comandos para migração

docker exec -it papadobradofc_app bash
flask db init
flask db migrate -m "Criando tabelas iniciais"
flask db upgrade

# Cria o usuário e concede permissões
CREATE USER IF NOT EXISTS 'papadobradofc'@'%' IDENTIFIED BY 'Senh4ppfc';
GRANT ALL PRIVILEGES ON papadobradofc.* TO 'papadobradofc'@'%';
FLUSH PRIVILEGES;