#!/bin/bash
# visualization.sh

set -e 

echo "[VISUALIZATION]- Empezando Programa"
echo "[VISUALIZATION]- Preparando graphics/"
mkdir -p graphics
rm -rf graphics/*

echo "[VISUALIZATION]- Creando .venv"
python -m venv .venv
echo "[VISUALIZATION]- Activando .venv"
source .venv/bin/activate

echo "[VISUALIZATION]- Descargando Dependencias"
pip install -r requirements.txt

echo "[VISUALIZATION]- Creando Gráficos"
python ./scripts/plotting.py

echo "[VISUALIZATION]- Creando Tablas con medias"
python ./scripts/tables.py

echo "[VISUALIZATION]- Creando Tabla Global"
python ./scripts/global.py

echo "[VISUALIZATION]- Borrando .venv"
deactivate
rm -rf .venv

echo "[VISUALIZATION]- PROGRAMA FINALIZADO"
