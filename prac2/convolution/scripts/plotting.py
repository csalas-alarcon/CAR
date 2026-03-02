import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# CONSTANTES
DATA_DIR = "./metrics/processed"
GRAPHICS_DIR = "./graphics/plots/"
METRICS = ["base_O0", "base_O3", "simd_O0", "simd_O3"]
DEVICES = {
    "pc_aula": "Aula",
    "pc_carlos": "Carlos",
    "pc_jose": "Jose"
}
# Colores para las sub-categorías de tiempo
COLORS = {
    "Tiempo carga desde disco": "#3498db",
    "Tiempo de convolución (CPU)": "#e67e22",
    "Tiempo guardado en disco": "#2ecc71",
    "Tiempo total de ejecución": "#e74c3c"
}

def generate_performance_plots():
    if not os.path.exists(GRAPHICS_DIR):
        os.makedirs(GRAPHICS_DIR)

    for metric in METRICS:
        data_frames = []
        
        for folder, device_label in DEVICES.items():
            file_path = f"{DATA_DIR}/{folder}/{metric}.csv"
            
            if os.path.exists(file_path):
                # Leemos el CSV (delimitado por tabulaciones según tus prompts anteriores)
                df = pd.read_csv(file_path, sep='\t')
                # Pivotamos para tener los conceptos como columnas y una fila con los valores
                df_pivoted = df.set_index('Concepto').T
                df_pivoted['Device'] = device_label
                data_frames.append(df_pivoted)
        
        if not data_frames:
            print(f"No se encontraron datos para la métrica: {metric}")
            continue

        # Unimos los datos de todos los PCs para esta métrica
        final_df = pd.concat(data_frames).set_index('Device')
        
        # Configuración del gráfico de barras agrupadas
        ax = final_df.plot(kind='bar', 
                          figsize=(12, 7), 
                          color=[COLORS.get(col, '#333333') for col in final_df.columns],
                          width=0.8)

        # Formato
        plt.title(f"Comparativa de Rendimiento: {metric.replace('_', ' ').upper()}", fontsize=16)
        plt.ylabel("Tiempo (segundos)", fontsize=12)
        plt.xlabel("Dispositivo", fontsize=12)
        plt.xticks(rotation=0)
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.legend(title="Fases", bbox_to_anchor=(1.05, 1), loc='upper left')
        
        # Añadir etiquetas de valor sobre las barras
        for p in ax.patches:
            ax.annotate(f"{p.get_height():.2f}", 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', 
                        xytext=(0, 9), 
                        textcoords='offset points',
                        fontsize=8)

        plt.tight_layout()
        
        save_path = f"{GRAPHICS_DIR}plot_{metric}.png"
        plt.savefig(save_path, dpi=300)
        print(f"Generado: {save_path}")
        plt.close()

if __name__ == "__main__":
    generate_performance_plots()