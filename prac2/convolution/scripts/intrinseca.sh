echo "[INTRINSICA]- Compilando Proyecto con Librerias" 
g++ src/intrinseca.cpp -o bin/intrinseca_conv_O0 -Ivendor -std=c++17 -O0 -msse4.1 -lstdc++fs
g++ src/intrinseca.cpp -o bin/intrinseca_conv_O3 -Ivendor -std=c++17 -O3 -msse4.1 -lstdc++fs

echo "[INTRINSECA]- Ejecutando Programa con O0"
./bin/intrinseca_conv_O0 > tiempos/intrinseca_O0.txt
echo "[INTRINSECA]- Ejecutando Programa con 03"
./bin/intrinseca_conv_O3 > tiempos/intrinseca_O3.txt
