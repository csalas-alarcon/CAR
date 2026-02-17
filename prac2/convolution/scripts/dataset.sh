#!/bin/bash
# dataset.sh

set -e

echo "[DATA]- Creando directorio data/"
mkdir -p data
cd data

if [ -d "jpg" ] && [ "$(ls -A jpg)" ]; then
    echo "[DATA]- Dataset ya existe, saltando descarga."
else
    echo "[DATA]- Descargando Dataset de Flores"
    curl -L -o flowers.tgz https://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz

    echo "[DATA]- Extrayendo Dataset"
    tar -xzf flowers.tgz

    echo "[DATA]- Limpiando Comprimidos]"
    rm flowers.tgz
fi

echo "[DATA]- Dataset listo en data/jpg/"
