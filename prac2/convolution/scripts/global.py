import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# CONSTANTES
DATA_DIR = "./metrics/processed"
GRAPHICS_DIR = "./graphics/tables/"
DEVICES = {
    "pc_aula": "Aula",
    "pc_carlos": "Sala",
    "pc_jose": "Personal"
}
METRICS = ["base_O3", "simd_O3"]

def calculate_geometric_mean(series):
    clean_series = series[series > 0]
    return np.exp(np.log(clean_series).mean())

def generate_global_table():
    if not os.path.exists(GRAPHICS_DIR):
        os.makedirs(GRAPHICS_DIR)

    cell_data = []
    times = []

    # Recorrer métricas y dispositivos para juntar los 6 valores
    for metric in METRICS:
        for folder, device_label in DEVICES.items():
            file_path = f"{DATA_DIR}/{folder}/{metric}.csv"
            
            if not os.path.exists(file_path):
                continue

            df = pd.read_csv(file_path, sep='\t')
            
            # Extraer solo el tiempo total
            total_row = df[df['Concepto'] == 'Tiempo total de ejecución']
            if not total_row.empty:
                val = total_row.iloc[0]['Tiempo (s)']
                row_name = f"{metric}_{device_label}"
                cell_data.append([row_name, f"{val:.4f}"])
                times.append(val)
    
    if not times:
        print("No se encontraron datos para procesar.")
        return
        
    # Calcular medias de los 6 valores
    times_series = pd.Series(times)
    ma_time = times_series.mean()
    gm_time = calculate_geometric_mean(times_series)
    
    # Añadir filas de resumen
    cell_data.append(["Arithmetic Mean", f"{ma_time:.4f}"])
    cell_data.append(["Geometric Mean (GM)", f"{gm_time:.4f}"])

    # Crear Tabla
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.axis('off')
    
    columns = ["Versión", "Tiempo Total (s)"]
    
    table = ax.table(cellText=cell_data, 
                    colLabels=columns, 
                    loc='center', 
                    cellLoc='left')
    
    # Estilo
    table.auto_set_font_size(False)
    table.set_fontsize(11)
    table.scale(1.2, 1.8) 
    
    for (row, col), cell in table.get_celld().items():
        if row == 0: 
            cell.set_text_props(weight='bold', color='white')
            cell.set_facecolor('#2c3e50')
        elif row > len(times): # Filas de medias
            cell.set_text_props(weight='bold')
            if row == len(cell_data): # Fila GM (última) en rojo
                cell.set_text_props(color='red')

    plt.title("Resumen Global O3", pad=20, fontsize=14, weight='bold')
    
    # Guardar
    save_name = f"{GRAPHICS_DIR}table_global_O3_summary.png"
    plt.savefig(save_name, bbox_inches='tight', dpi=300)
    plt.close()
    print(f"Tabla generada: {save_name}")

if __name__ == "__main__":
    generate_global_table()