FROM python:3.12-slim

WORKDIR /usr/src/app

# Instala pacotes essenciais e configura localidade
RUN apt-get update && apt-get install -y locales netcat-openbsd \
    && echo "pt_BR.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen pt_BR.UTF-8 \
    && apt-get clean

# Configura a localidade para pt_BR.UTF-8
ENV LC_ALL=pt_BR.UTF-8
ENV LANG=pt_BR.UTF-8
ENV LANGUAGE=pt_BR.UTF-8

# Configura variáveis do Flask
ENV FLASK_APP="app.app:app"
ENV FLASK_ENV="development"
ENV SECRET_KEY="9870e1457b4e12f21224f6c4354f41ff9cfea58070414c8b"
ENV FLASK_DEBUG=1

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .