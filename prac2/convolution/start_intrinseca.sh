#!/bin/bash
# start_intrinseca.sh

#   _____ _________    ____  _______
#  / ___//_  __/   |  / __ \/_  __/ 
#  \__ \  / / / /| | / /_/ / / /  
# ___/ / / / / ___ |/ _, _/ / / 
#/____/ /_/ /_/  |_/_/ |_| /_/ 
#                                       
#  Automated Build & Execution Script
# -----------------------------------------------------------------------------
#  Binary: bin/convolucion_intrinseca
#  Output: ./output_intrinseca/
# -----------------------------------------------------------------------------


set -e

echo "[START]- Llamando Script de Descarga"
./scripts/dataset.sh

echo "[START]- Preparando output_intrinseca/"
mkdir -p output_intrinseca
rm -f output_intrinseca/*

echo "[START]- Preparando bin_intrinseca/"
mkdir -p bin_intrinseca
rm -f bin_intrinseca/*

echo "[START]- Compilando Proyecto con Librerias" 
g++ src/main_intrinseca.cpp -o bin_intrinseca/convolucion_intrinseca -Ivendor -std=c++17 -O3 -msse4.1 -lstdc++fs

echo "[START]- Ejecutando Programa"
./bin_intrinseca/convolucion_intrinseca