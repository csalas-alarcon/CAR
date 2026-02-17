
// Importaciones sbt  - Libreria de Sean Burry
#define STB_IMAGE_IMPLEMENTATION // Definimos un macro
#include "stb_image.h" // que se encuentra definido aquí.
#define STB_IMAGE_WRITE_IMPLEMENTATION // Lo mismo que antes
#include "stb_image_write.h"

// Importaciones std
#include <iostream>
#include <vector>
#include <filesystem>
#include <algorithm> // Para std::min y std::max
#include <chrono> // Para medir tiempos

// Simple namespace
using namespace std;

// Constantes
#define INPUT_CHANNELS 3
#define OUTPUT_DIRECTORY "./output/"

// --- Kernel: Desenfoque de caja (Box Blur) ---
vector<vector<float>> box_blur = {
    {1.0f/9.0f, 1.0f/9.0f, 1.0f/9.0f},
    {1.0f/9.0f, 1.0f/9.0f, 1.0f/9.0f},
    {1.0f/9.0f, 1.0f/9.0f, 1.0f/9.0f}
};

// --- Kernel: Detección de Bordes (Sobel Horizontal) ---
vector<vector<float>> sobel_h = {
    { 1.0f,  2.0f,  1.0f},
    { 0.0f,  0.0f,  0.0f},
    {-1.0f, -2.0f, -1.0f}
};

// --- Kernel: Filtro de Repujado (Emboss) ---
vector<vector<float>> emboss = {
    {-2.0f, -1.0f, 0.0f},
    {-1.0f,  1.0f, 1.0f},
    { 0.0f,  1.0f, 2.0f}
};

// --- Kernel: Desenfoque Gaussiano (5x5) ---
vector<vector<float>> kernel = {
    {1/256.0f,  4/256.0f,  6/256.0f,  4/256.0f, 1/256.0f},
    {4/256.0f, 16/256.0f, 24/256.0f, 16/256.0f, 4/256.0f},
    {6/256.0f, 24/256.0f, 36/256.0f, 24/256.0f, 6/256.0f},
    {4/256.0f, 16/256.0f, 24/256.0f, 16/256.0f, 4/256.0f},
    {1/256.0f,  4/256.0f,  6/256.0f,  4/256.0f, 1/256.0f}
};

// Structuras de Información
struct Imagen {
    int w, h, c;
    unsigned char* data;
};

// FUNCIONES
vector<string> obtener_rutas_imagenes(const string& carpeta) {
    std::vector<string> archivos;

    for (const auto& entry : filesystem::directory_iterator(carpeta)) {
        if (!entry.is_regular_file()) continue;

        string ext = entry.path().extension().string();
        if (ext == ".png" || ext == ".jpg" || ext == ".jpeg" ||
            ext == ".bmp" || ext == ".tga") {
            archivos.push_back(entry.path().string());
        }
    }
    return archivos;
}

Imagen applicar_kernel(const Imagen& entrada, const vector<vector<float>>& kernel) {
    int k_h = kernel.size(); // Conseguimos Altura del Kernel
    int k_w = kernel[0].size(); // Conseguimos Anchura del Kernel

    Imagen salida; // Instanciamos la Salida con el Struct Imagen
    // Empequenyecemos la salida para evitar salirse de la imagen.
    salida.w = entrada.w - k_w + 1; 
    salida.h = entrada.h - k_h + 1;
    salida.c = entrada.c;
    // // Definimos el tamanyo de la imagen en Unsigned Chars.
    salida.data = new unsigned char[salida.w * salida.h * salida.c];

    // Para cada combinación de Y y X
    for (int y = 0; y < salida.h; y++) {
        for (int x = 0; x < salida.w; x++) {
            // Para cada Canal
            for (int c = 0; c < salida.c; c++) {
                float suma = 0.0f;

                // Para cada Y y X del Kernel
                for (int ky = 0; ky < k_h; ky++) {
                    for (int kx = 0; kx < k_w; kx++) {
                        // Calculamos el Indice en Data
                        int ix = x + kx;
                        int iy = y + ky;
                        // Nos saltamos iy lineas + ix desplazamiento en la linea
                        // * el número de Canales más el Offset
                        int idx = (iy * entrada.w + ix) * entrada.c + c;
                        // Multiplicamos el Kernel por el valor correspondiente
                        suma += kernel[ky][kx] * (float)entrada.data[idx];
                    }
                }

                // Calculamos el Indice en Data
                int out_idx = (y * salida.w + x) * salida.c + c;
                suma = min(255.0f, max(0.0f, suma)); // Clamping Evitamos Desbordamientos
                // Asignamos el Valor
                salida.data[out_idx] = (unsigned char) suma;
            }
        }
    }
    return salida;
}

// PUNTO DE ENTRADA
int main() {
    // Consigue direcciones de imagenes
    vector<string> paths = obtener_rutas_imagenes("./../imgs/jpg/");

    // Itera sobre cada dirección
    for (const string& path : paths) {
        // Instancia Struct
        Imagen img;
        // Assigna un pointer ...
        img.data = stbi_load(path.c_str(), &img.w, &img.h, &img.c, INPUT_CHANNELS);

        // Comprobar si se ha leido correctamente
        if (img.data == NULL) {
            std::cerr << "No se pudo cargar: " << path << endl;
            exit(-1);
        }
        

        
        /*
        * Aplicar el algoritmo de la convolución AQUI
        */
        Imagen output_img;
        const int output_channels = INPUT_CHANNELS; // Cambiar si hay canales de salida diferentes

        printf("Imagen: %s, w: %i, h: %i, c: %i\n", path.c_str(), img.w, img.h, img.c);



        // Escribir imagen
        string new_path = "conv_" + path.substr(path.find_last_of("/\\") + 1);;
        new_path = OUTPUT_DIRECTORY + new_path;
        //int resultado_escritura = stbi_write_jpg(new_path.c_str(), output_img.w, output_img.h, output_channels, output_img.data, 50);
        int resultado_escritura = stbi_write_jpg(new_path.c_str(), img.w, img.h, img.c, img.data, 50);

        if (resultado_escritura == 0) {
            std:cerr << "Error: no se ha podido escribir el archivo " << new_path << endl;
            exit(-1);
        }

        // Liberar memoria imagen
        stbi_image_free(img.data);
    }
    return 0;
}