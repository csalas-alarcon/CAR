# Arquitectura y Flujo de Datos
Por Jose Francisco Hurtado Valero
y Carlos Salas Alarcón
---

El proyecto automatiza la evaluación de rendimiento usando *scripts* en la raíz (`root`) de cada módulo que orquestan el trabajo llamando a archivos específicos dentro de sus subcarpetas.

## 1. Módulo: Convolution

* **`start.sh` (en el root):** Es el orquestador principal. Primero, crea las carpetas vacías `bin/`, `output/` (con sus subcarpetas `base/` e `intrinseca/`) y `tiempos/`. Después, llama a los siguientes *scripts* ubicados en la carpeta `scripts/`:
* **Llama a `scripts/dataset.sh`:** Este archivo descarga el comprimido de internet y extrae las imágenes directamente en la carpeta `dataset/jpg/`.
* **Llama a `scripts/base.sh` e `scripts/intrinseca.sh`:** Estos *scripts* leen el código fuente de `src/` usando las librerías de `vendor/`, compilan los programas y guardan los ejecutables resultantes en `bin/`. Inmediatamente después, ejecutan esos binarios y redirigen los resultados de tiempo para guardarlos como archivos `.txt` en la carpeta `tiempos/`.


* **`visualization.sh` (en el root):** Lee el archivo `requirements.txt` (también en el root) para instalar las dependencias de Python. Luego, crea la carpeta `graphics/` y ejecuta los *scripts* de Python (`plotting.py`, `tables.py`, etc.) guardados en `scripts/`. Estos programas procesan los datos tabulados en `data/processed/`y guardan las gráficas generadas en `graphics/`.

## 2. Módulo: Speccpu

* **`start.sh` (en el root):** Instala las dependencias leyendo `requirements.txt`. Luego, crea la carpeta vacía `graphics/` y ejecuta los *scripts* de Python ubicados en `scripts/` (`visualize.py` y `tables.py`).
* **Flujo de los *scripts* de Python:** Estos archivos leen los datos tabulados en `data/processed/`, los procesan y finalmente guardan las gráficas generadas en la carpeta `graphics/`.

---

## Árbol de Directorios

```text
.
├── convolution/
│   ├── bin/
│   │   └── Ejecutables compilados...
│   ├── dataset/
│   │   └── jpg/
│   │       └── .jpg files...
│   ├── graphics/
│   │   └── .png files...
│   ├── output/
│   │   ├── base/
│   │   │   └── Archivos de salida...
│   │   └── intrinseca/
│   │       └── Archivos de salida...
│   ├── tiempos/
│   │   └── .txt files...
│   ├── data/
│   │   ├── processed/
│   │   │   └── .csv files...
│   │   └── raw/
│   │       └── .txt files...
│   ├── src/
│   │   └── .cpp files...
│   ├── vendor/
│   │   └── .h files...
│   ├── scripts/
│   │   └── .sh y .py files...
│   ├── requirements.txt
│   ├── visualization.sh
│   └── start.sh
├── speccpu/
│   ├── data/
│   │   ├── processed/
│   │   │   └── .csv files...
│   │   └── raw/
│   │       └── .txt files...
│   ├── graphics/
│   │   └── .png files...
│   ├── scripts/
│   │   └── .py files...
│   ├── requirements.txt
│   └── start.sh
└── README.md

```