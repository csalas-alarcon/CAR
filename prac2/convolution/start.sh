#!/bin/bash
# start.sh

#   _____ _________    ____  _______
#  / ___//_  __/   |  / __ \/_  __/ 
#  \__ \  / / / /| | / /_/ / / /  
# ___/ / / / / ___ |/ _, _/ / / 
#/____/ /_/ /_/  |_/_/ |_| /_/ 
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

echo "[START]- Preparando tiempos/"
mkdir -p tiempos
rm -f tiempos/*

echo "[START]- Compilando Proyecto con Librerias" 
g++ -std=c++17 src/main.cpp -I./vendor -o bin/image_conv_O0 -O0
g++ -std=c++17 src/main.cpp -I./vendor -o bin/image_conv_O3 -O3

echo "[START]- Ejecutando Programa"
./bin/image_conv_O0 > tiempos/main_O0.txt
./bin/image_conv_O3 > tiempos/main_O3.txt