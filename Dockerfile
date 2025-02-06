# Usando a versão mais recente e leve do Python
FROM python:3.12-slim

# Definir o diretório de trabalho
WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc libc-dev libssl-dev libffi-dev && \
    rm -rf /var/lib/apt/lists/*

# Copiar e instalar dependências do Python
COPY app/requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Copiar os arquivos do projeto
COPY . .

# Expor a porta que será usada
EXPOSE 8282

# Definir variáveis de ambiente
ENV FLASK_APP=main.py
ENV FLASK_ENV=production

# Iniciar a aplicação com Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8282", "app.main:app"]
