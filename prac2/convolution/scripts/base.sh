echo "[BASE]- Compilando Proyecto con Librerias" 
g++ -std=c++17 src/base.cpp -I./vendor -o bin/base_conv_O0 -O0
g++ -std=c++17 src/base.cpp -I./vendor -o bin/base_conv_O3 -O3

echo "[BASE]- Ejecutando Programa con O0"
./bin/base_conv_O0 > tiempos/base_O0.txt
echo "[BASE]- Ejecutando Programa con O3"
./bin/base_conv_O3 > tiempos/base_O3.txt