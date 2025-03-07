#!/bin/bash

echo "🚀 Parando e removendo containers antigos..."
docker-compose down -v
docker system prune -a --volumes -f

echo "🔨 Construindo e subindo os containers..."
docker-compose up -d --build
