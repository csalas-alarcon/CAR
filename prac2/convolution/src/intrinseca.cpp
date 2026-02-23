
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
#include <immintrin.h> // Cabecera para intrínsecas (SSE)

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
#define OUTPUT_DIRECTORY "./output/intrinseca/"

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
    int k_h = kernel.size();
    int k_w = kernel[0].size();

    Imagen salida;
    salida.w = entrada.w - k_w + 1; 
    salida.h = entrada.h - k_h + 1;
    salida.c = entrada.c; // Sabemos que es 3 (RGB)
    salida.data = new unsigned char[salida.w * salida.h * salida.c];

    // Bucle Y y X (Recorremos la imagen de salida)
    for (int y = 0; y < salida.h; y++) {
        for (int x = 0; x < salida.w; x++) {
            
            // --- PASO 1: Preparar la "Caja" SSE ---
            // _mm_setzero_ps() crea un vector de 4 floats inicializados a 0.0f
            // Contendrá: [Suma_R, Suma_G, Suma_B, 0.0]
            __m128 sum_vec = _mm_setzero_ps();

            // Recorremos la ventana del Kernel
            for (int ky = 0; ky < k_h; ky++) {
                for (int kx = 0; kx < k_w; kx++) {
                    
                    int ix = x + kx;
                    int iy = y + ky;
                    int idx = (iy * entrada.w + ix) * entrada.c; // Índice base del píxel

                    // --- PASO 2: Cargar y empaquetar los 3 canales ---
                    // Extraemos los valores unsigned char y los pasamos a float
                    float r = (float)entrada.data[idx];
                    float g = (float)entrada.data[idx + 1];
                    float b = (float)entrada.data[idx + 2];

                    // _mm_set_ps empaqueta 4 floats en un registro SSE.
                    // ATENCIÓN: Esta función recibe los argumentos en orden inverso (w, z, y, x)
                    // Así que le pasamos (Vacio, B, G, R) para que queden en orden normal en memoria.
                    __m128 pixel_vec = _mm_set_ps(0.0f, b, g, r);

                    // --- PASO 3: Preparar el valor del kernel ---
                    // _mm_set1_ps copia un único valor en los 4 huecos del registro.
                    // Queda así: [Kernel_val, Kernel_val, Kernel_val, Kernel_val]
                    __m128 kernel_vec = _mm_set1_ps(kernel[ky][kx]);

                    // --- PASO 4: Multiplicar y Acumular ---
                    // _mm_mul_ps: Multiplica pixel_vec * kernel_vec (los 4 a la vez)
                    // _mm_add_ps: Se lo suma a sum_vec (los 4 a la vez)
                    __m128 prod = _mm_mul_ps(pixel_vec, kernel_vec);
                    sum_vec = _mm_add_ps(sum_vec, prod);
                }
            }

            // --- PASO 5: Desempaquetar el resultado ---
            // Sacamos los 4 floats del registro SSE a un array normal de C++
            float sums[4];
            _mm_storeu_ps(sums, sum_vec);

            // --- PASO 6: Guardar en la imagen de salida ---
            int out_idx = (y * salida.w + x) * salida.c;
            
            // Hacemos el clamping (0-255) y guardamos R, G y B.
            // sums[0] es R, sums[1] es G, sums[2] es B.
            salida.data[out_idx]     = (unsigned char)min(255.0f, max(0.0f, sums[0]));
            salida.data[out_idx + 1] = (unsigned char)min(255.0f, max(0.0f, sums[1]));
            salida.data[out_idx + 2] = (unsigned char)min(255.0f, max(0.0f, sums[2]));
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