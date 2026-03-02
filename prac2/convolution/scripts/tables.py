import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# CONSTANTS
DATA_DIR = "./metrics/processed"
GRAPHICS_DIR = "./graphics/tables/"
DEVICES = {
    "pc_aula": "Aula",
    "pc_carlos": "Carlos",
    "pc_jose": "Jose"
}
METRICS = ["base_O3", "simd_O3"]

def calculate_geometric_mean(series):
    clean_series = series[series > 0]
    return np.exp(np.log(clean_series).mean())

def generate_performance_tables():
    if not os.path.exists(GRAPHICS_DIR):
        os.makedirs(GRAPHICS_DIR)

    for folder, device_label in DEVICES.items():
        cell_data = []
        times = []
        
        for metric in METRICS:
            file_path = f"{DATA_DIR}/{folder}/{metric}.csv"
            
            if not os.path.exists(file_path):
                continue

            df = pd.read_csv(file_path, sep='\t')
            
            # Extract only the total execution time
            total_row = df[df['Concepto'] == 'Tiempo total de ejecución']
            if not total_row.empty:
                val = total_row.iloc[0]['Tiempo (s)']
                cell_data.append([metric.upper(), f"{val:.4f}"])
                times.append(val)
        
        if not times:
            continue
            
        # Calculate means
        times_series = pd.Series(times)
        ma_time = times_series.mean()
        gm_time = calculate_geometric_mean(times_series)
        
        # Add summary rows
        cell_data.append(["Arithmetic Mean", f"{ma_time:.4f}"])
        cell_data.append(["Geometric Mean (GM)", f"{gm_time:.4f}"])

        # Create Table
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.axis('off')
        
        columns = ["Versión", "Tiempo Total (s)"]
        
        table = ax.table(cellText=cell_data, 
                        colLabels=columns, 
                        loc='center', 
                        cellLoc='left')
        
        # Styling
        table.auto_set_font_size(False)
        table.set_fontsize(11)
        table.scale(1.2, 1.8) 
        
        for (row, col), cell in table.get_celld().items():
            if row == 0: 
                cell.set_text_props(weight='bold', color='white')
                cell.set_facecolor('#2c3e50')
            elif row > len(times): # Summary rows
                cell.set_text_props(weight='bold')
                if row == len(cell_data): # GM row in red
                    cell.set_text_props(color='red')

        plt.title(f"Resumen O3: {device_label}", pad=20, fontsize=14, weight='bold')
        
        # Save
        save_name = f"{GRAPHICS_DIR}table_{folder}_O3_summary.png"
        plt.savefig(save_name, bbox_inches='tight', dpi=300)
        plt.close()
        print(f"Tabla generada: {save_name}")

if __name__ == "__main__":
    generate_performance_tables()