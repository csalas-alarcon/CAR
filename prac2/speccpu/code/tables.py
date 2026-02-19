import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

# CONSTANTS
DATA_DIR = "./metrics/processed"  # Adjusted based on your tree (code/ is a subfolder)
GRAPHICS_DIR = "./graphics/"
DEVICES = {
    "pc_pc": "Sala",
    "pc_clase": "Aula",
    "pc_personal": "Personal"
}
METRICS = ["cint_base", "cint_peak", "cfp_base", "cfp_peak"]

def calculate_geometric_mean(series):
    return np.exp(np.log(series).mean())

def generate_spec_tables():
    if not os.path.exists(GRAPHICS_DIR):
        os.makedirs(GRAPHICS_DIR)

    for folder, device_label in DEVICES.items():
        for metric in METRICS:
            file_path = f"{DATA_DIR}/{folder}/{metric}.csv"
            
            if not os.path.exists(file_path):
                continue

            # 1. Load and identify columns
            df = pd.read_csv(file_path, sep='\t')
            # Dynamic column detection
            bench_col = [c for c in df.columns if 'Bench' in c][0]
            ref_col = [c for c in df.columns if 'Ref' in c][0]
            run_col = [c for c in df.columns if 'Run' in c][0]
            ratio_col = [c for c in df.columns if 'Ratio' in c][0]

            # 2. Calculate Summary Rows
            ma_tr = df[ref_col].mean()
            ma_te = df[run_col].mean()
            ma_ratio = df[ratio_col].mean()
            geomean_ratio = calculate_geometric_mean(df[ratio_col])

            # 3. Prepare data for the Table
            # Create a copy for display to avoid modifying original data
            table_df = df[[bench_col, ref_col, run_col, ratio_col]].copy()
            
            # Add summary rows
            summaries = [
                ["MA(TR)", f"{ma_tr:.2f}", "", ""],
                ["MA(TE)", "", f"{ma_te:.2f}", ""],
                ["MA(TR/TE)", "", "", f"{ma_ratio:.2f}"],
                ["SPEC Score (GeoMean)", "", "", f"**{geomean_ratio:.2f}**"]
            ]
            
            # 4. Plotting the Table
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.axis('off')
            
            # Prepare data list for matplotlib table
            cell_data = table_df.values.tolist() + summaries
            columns = ["Benchmark", "Ref Time", "Run Time", "Ratio"]

            table = ax.table(cellText=cell_data, 
                            colLabels=columns, 
                            loc='center', 
                            cellLoc='center')
            
            # Styling
            table.auto_set_font_size(False)
            table.set_fontsize(10)
            table.scale(1.2, 1.5) # Stretch for readability
            
            # Bold the header and the final score
            for (row, col), cell in table.get_celld().items():
                if row == 0: # Header
                    cell.set_text_props(weight='bold')
                if row == len(cell_data): # Last row (GeoMean)
                    cell.set_text_props(weight='bold', color='red')

            plt.title(f"SPEC Summary: {device_label} - {metric.upper()}", pad=20, fontsize=14, weight='bold')
            
            # Save Output
            save_name = f"{GRAPHICS_DIR}table_{device_label.lower()}_{metric}.png"
            plt.savefig(save_name, bbox_inches='tight', dpi=300)
            plt.close()
            print(f"Generated Table: {save_name}")

if __name__ == "__main__":
    generate_spec_tables()