
// Importaciones sbt  - Libreria de Sean Burry
#define STB_IMAGE_IMPLEMENTATION // Definimos un macro
#include "stb_image.h" // que se encuentra definido aquí.
#define STB_IMAGE_WRITE_IMPLEMENTATION // Lo mismo que antes
#include "stb_image_write.h"

// Importaciones std
#include <iostream>
#include <vector>
#include <filesystem>

// Simple namespace
using namespace std;

// CONSTANTS
#define INPUT_CHANNELS 3
#define OUTPUT_DIRECTORY "./output/"

// DATA Structures
struct Imagen {
    int w, h, c;
    unsigned char* data;
};

/**
 * Obtener todas las rutas de las imágenes dentro de una carpeta.
 *
 * Parameters
 * ----------
 * carpeta : const std::string&
 *     Ruta de la carpeta que contiene las imágenes.
 *
 * Returns
 * -------
 * std::vector<std::string>
 *     Vector de strings con las rutas completas de las imágenes que tienen
 *     extensiones válidas: ".png", ".jpg", ".jpeg", ".bmp", ".tga".
 *
 * Notes
 * -----
 * Esta función utiliza C++17 std::filesystem para iterar sobre los archivos
 * de la carpeta. Solo se incluyen archivos regulares; los directorios o
 * enlaces simbólicos son ignorados. La función filtra las imágenes según
 * su extensión y devuelve sus rutas completas como strings.
 *
 * Example
 * -------
 * std::vector<std::string> images = obtener_rutas_imagenes("./data/");
 * for (const auto& path : images) {
 *     std::cout << path << std::endl;
 * }
*/

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