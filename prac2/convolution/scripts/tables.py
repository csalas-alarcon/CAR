import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# CONSTANTES
DATA_DIR = "./metrics/processed"
GRAPHICS_DIR = "./graphics/tables/"
DEVICES = {
    "pc_aula": "Aula",
    "pc_carlos": "Carlos",
    "pc_jose": "Jose"
}
METRICS = ["base_O0", "base_O3", "simd_O0", "simd_O3"]

def calculate_geometric_mean(series):
    # Filtramos valores <= 0 para evitar errores en logaritmos
    clean_series = series[series > 0]
    return np.exp(np.log(clean_series).mean())

def generate_performance_tables():
    if not os.path.exists(GRAPHICS_DIR):
        os.makedirs(GRAPHICS_DIR)

    for folder, device_label in DEVICES.items():
        for metric in METRICS:
            file_path = f"{DATA_DIR}/{folder}/{metric}.csv"
            
            if not os.path.exists(file_path):
                continue

            # 1. Carga de datos (TSV)
            df = pd.read_csv(file_path, sep='\t')
            
            # 2. Cálculos de Resumen
            # Usamos la columna 'Tiempo (s)' para las métricas
            time_col = "Tiempo (s)"
            
            ma_time = df[time_col].mean()
            gm_time = calculate_geometric_mean(df[time_col])

            # 3. Preparar datos para la tabla visual
            # Convertimos a lista de listas para Matplotlib
            cell_data = df.values.tolist()
            
            # Añadimos filas de resumen
            cell_data.append(["Arithmetic Mean", f"{ma_time:.4f}"])
            cell_data.append(["Geometric Mean (GM)", f"{gm_time:.4f}"])
            
            # 4. Creación de la imagen de la Tabla
            fig, ax = plt.subplots(figsize=(8, 5))
            ax.axis('off')
            
            columns = ["Concepto", "Tiempo (s)"]
            
            table = ax.table(cellText=cell_data, 
                            colLabels=columns, 
                            loc='center', 
                            cellLoc='left')
            
            # Estilo
            table.auto_set_font_size(False)
            table.set_fontsize(11)
            table.scale(1.2, 1.8) # Ajuste de celdas para legibilidad
            
            # Resaltar cabecera y totales
            for (row, col), cell in table.get_celld().items():
                if row == 0: # Cabecera
                    cell.set_text_props(weight='bold', color='white')
                    cell.set_facecolor('#2c3e50')
                if row > len(df): # Filas de medias
                    cell.set_text_props(weight='bold')
                    if row == len(cell_data): # GM en rojo como en tu inspiración
                        cell.set_text_props(color='red')

            plt.title(f"Resumen de Tiempos: {device_label} ({metric.upper()})", 
                      pad=20, fontsize=14, weight='bold')
            
            # Guardar
            save_name = f"{GRAPHICS_DIR}table_{folder}_{metric}.png"
            plt.savefig(save_name, bbox_inches='tight', dpi=300)
            plt.close()
            print(f"Tabla generada: {save_name}")

if __name__ == "__main__":
    generate_performance_tables()