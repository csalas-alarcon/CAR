
// sbt Imports
#define STB_IMAGE_IMPLEMENTATION
#include "stb_image.h"
#define STB_IMAGE_WRITE_IMPLEMENTATION
#include "stb_image_write.h"

// std imports
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

/*
*
* Esta función obtiene todas las rutas de las imágenes dentro de una carpeta
*
* Input:
*     - string carpeta: String con la ruta de la carpeta que contiene las imágenes
*
* Output:
*     - vector<string>: Vector de strings con las rutas de las imágenes
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

    vector<string> paths = obtener_rutas_imagenes("./Birds_25/train/Asian-Green-Bee-Eater/");

    for (const string& path : paths) {
        // Cargar imagen
        Imagen img;
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