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
mkdir -p output/{base,intrinseca}
rm -f output/base/*
rm -f output/intrinseca/*

echo "[START]- Preparando bin/"
mkdir -p bin
rm -f bin/*

echo "[START]- Preparando tiempos/"
mkdir -p tiempos/
rm -f tiempos/*

echo "[START]- Llamando a Convolucion BASE"
./scripts/base.sh 
echo "[START]- Llamando a Convolucion INTRINSECA"
./scripts/intrinseca.sh

echo "[START]- Programa Finalizado"