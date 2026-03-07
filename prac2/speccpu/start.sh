#!/bin/bash
# start.sh

echo '[START]- EMPEZANDO PROGRAMA'

echo '[START]- Creando y Preparando graphics/'
mkdir -p graphics/
rm -rf graphics/*

echo '[START]- Creando Entorno Virtual .venv'
python -m venv .venv 

echo '[START]- Activando .venv'
source .venv/bin/activate 

echo '[START]- Descargando Dependencias'
pip install -r requirements.txt

echo '[START]- Ejecutando Script de Gráficas'
python scripts/visualize.py
echo '[START]- Ejecutando Script de Tablas'
python scripts/tables.py

echo '[START]- Eliminando Entorno Virtual .venv'
deactivate
rm -rf .venv

echo '[START]- PROGRAMA FINALIZADO'
