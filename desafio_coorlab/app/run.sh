#!/bin/bash

# Instalação das dependências do frontend
echo "Instalando dependências do frontend..."
npm install

# Compilação do frontend
echo "Compilando o frontend..."
npm run build

# Instalando as dependências do Python:
echo "Instalando as dependências do Python necessárias para o projeto."
pip install flask axios

# Execução do servidor backend
echo "Iniciando o servidor backend..."
python app.py
