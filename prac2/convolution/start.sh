#!/bin/bash
# start.sh

#   _____ _________    ____  __________
#  / ___//_  __/   |  / __ \/_  __/ ___/
#  \__ \  / / / /| | / /_/ / / /  \__ \ 
# ___/ / / / / ___ |/ _, _/ / /  ___/ / 
#/____/ /_/ /_/  |_/_/ |_| /_/  /____/  
#                                       
#  Automated Build & Execution Script
# -----------------------------------------------------------------------------
#  Binary: bin/image_conv
#  Output: ./output/
# -----------------------------------------------------------------------------


set -e

echo "[START]- Llamando Script de Descarga"
./scripts/dataset.sh

echo "[START]- Preparando output/"
mkdir -p output
rm -f output/*

echo "[START]- Preparando bin/"
mkdir -p bin
rm -f bin/*

echo "[START]- Compilando Proyecto con Librerias" 
g++ -std=c++17 src/main.cpp -I./vendor -o bin/image_conv

echo "[START]- Ejecutando Programa"
./bin/image_conv