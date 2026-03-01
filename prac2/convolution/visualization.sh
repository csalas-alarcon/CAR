
set -e 

echo "[VISUALIZATION]- Empezando Programa"
echo "[VISUALIZATION]- Preparando graphics/"
mkdir -p graphics
rm -f graphics/*

echo "[VISUALIZATION]- Creando .venv"
python -m venv .venv
source .venv/bin/activate

echo "[VISUALIZATION]- Instalando Dependencias"
pip install -r requirements.txt

echo "[VISUALIZATION]- Creando Gráficos"
python ./scripts/plotting.py

echo "[VISUALIZATION]- Creando Tablas con medias"
python ./scripts/tables.py

echo "[VISUALIZATION]- Borrando .venv"
rm -rf .venv

echo "[VISUALIZATION]- PROGRAMA FINALIZADO"
