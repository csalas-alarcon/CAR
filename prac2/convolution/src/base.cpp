
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

// Structuras de Información
struct Imagen {
    int w, h, c;
    unsigned char* data;
};

struct Kernel {
    string name; 
    vector<vector<float>> data;
};

// Constantes
#define INPUT_CHANNELS 3
#define INPUT_DIRECTORY "./data/jpg/" //"./data/dataset_cats_dogs/PetImages/Dog" //"./data/jpg/"
#define OUTPUT_DIRECTORY "./output/base/"

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
vector<vector<float>> gauss = {
    {1/256.0f,  4/256.0f,  6/256.0f,  4/256.0f, 1/256.0f},
    {4/256.0f, 16/256.0f, 24/256.0f, 16/256.0f, 4/256.0f},
    {6/256.0f, 24/256.0f, 36/256.0f, 24/256.0f, 6/256.0f},
    {4/256.0f, 16/256.0f, 24/256.0f, 16/256.0f, 4/256.0f},
    {1/256.0f,  4/256.0f,  6/256.0f,  4/256.0f, 1/256.0f}
};

vector<Kernel> kernels = {
    {"blur", box_blur},
    {"sobel", sobel_h},
    {"emboss", emboss},
    {"gaussian", gauss},
};

// FUNCIONES
// Consigue Rutas de Archivos
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

// Aplica el Kernel
Imagen aplicar_kernel(const Imagen& entrada, const vector<vector<float>>& kernel) {
    int k_h = kernel.size(); // Conseguimos Altura del Kernel
    int k_w = kernel[0].size(); // Conseguimos Anchura del Kernel

    Imagen salida; // Instanciamos la Salida con el Struct Imagen
    // Empequenyecemos la salida para evitar salirse de la imagen.
    salida.w = entrada.w - k_w + 1; 
    salida.h = entrada.h - k_h + 1;
    salida.c = entrada.c;
    // Definimos el tamanyo de la imagen en Unsigned Chars.
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
    // --- INICIO: PREPARACIÓN DE CRONÓMETROS ---
    auto total_start = chrono::high_resolution_clock::now(); // Crono para el tiempo total

    // Acumuladores para cada fase
    chrono::duration<double> tiempo_carga_total(0);
    chrono::duration<double> tiempo_convolucion_total(0);
    chrono::duration<double> tiempo_guardado_total(0);
    
    // Consigue direcciones de imagenes
    vector<string> all_paths = obtener_rutas_imagenes(INPUT_DIRECTORY);
    // Nos quedamos solo con las 8 primeras
    vector<string> paths(all_paths.begin(), all_paths.begin() + 1000);

    int img_counter = 1;
    // Itera sobre cada dirección
    for (const string& path : paths) {
        // Crono 1 - Tiempo de carga
        auto start_carga = chrono::high_resolution_clock::now();

        Imagen img; // Nueva Instancia Imagen
        // Serializa la imagen a RGB
        img.data = stbi_load(path.c_str(), &img.w, &img.h, &img.c, INPUT_CHANNELS);

        auto end_carga = chrono::high_resolution_clock::now();
        tiempo_carga_total += (end_carga - start_carga);

        // Comprobar Error
        if (img.data == NULL) {
            std::cerr << "No se pudo cargar: " << path << endl;
            continue;
        }
        
        // PROCESAMIENTO / CONVOLUCION
        for (const auto& k : kernels) {
            // Crono 2 - Tiempo convolucion
            auto start_conv = chrono::high_resolution_clock::now();
            Imagen output_img = aplicar_kernel(img, k.data);
            auto end_conv = chrono::high_resolution_clock::now();
            tiempo_convolucion_total += (end_conv - start_conv);

            string new_name = k.name + "_" + to_string(img_counter) + ".jpg";
            string new_path = string(OUTPUT_DIRECTORY) + new_name;

            // Crono 3 - Tiempo guardado
            auto start_guardado = chrono::high_resolution_clock::now();
            int res = stbi_write_jpg(new_path.c_str(), output_img.w, output_img.h, output_img.c, output_img.data, 90);
            auto end_guardado = chrono::high_resolution_clock::now();
            tiempo_guardado_total += (end_guardado - start_guardado);

            if (res == 0) {
                std::cerr << "Error escribiendo: " << new_path << endl;
            } else {
                printf("Guardado: %s\n", new_name.c_str());
            }

            delete[] output_img.data;
        }
    
        stbi_image_free(img.data);
        img_counter ++;
    }

    auto total_end = chrono::high_resolution_clock::now();
    chrono::duration<double> tiempo_total = total_end - total_start;

    // --- RESUMEN FINAL DE TIEMPOS ---
    cout << "\n----------------------------------------" << endl;
    cout << "          RESUMEN DE TIEMPOS" << endl;
    cout << "----------------------------------------" << endl;
    cout << "Tiempo carga desde disco: " << tiempo_carga_total.count() << " s" << endl;
    cout << "Tiempo de convolución (CPU): " << tiempo_convolucion_total.count() << " s" << endl;
    cout << "Tiempo guardado en disco:  " << tiempo_guardado_total.count() << " s" << endl;
    cout << "----------------------------------------" << endl;
    cout << "Tiempo total de ejecución: " << tiempo_total.count() << " s" << endl;
    cout << "----------------------------------------" << endl;

    return 0;
}