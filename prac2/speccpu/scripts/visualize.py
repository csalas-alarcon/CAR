# Geneirc Imports
import pandas as pd
import matplotlib.pyplot as plt
import os

# CONSTANTS
DATA_DIR = "./metrics/processed"
GRAPHICS_DIR = "./graphics/"
COLORS = {"Sala": "tab:blue", "Aula": "tab:orange", "Personal": "tab:green"}
METRICS = ["cint_base", "cint_peak", "cfp_base", "cfp_peak"]
DEVICES = {
        "pc_pc": "Sala",
        "pc_clase": "Aula",
        "pc_personal": "Personal"
    }

def generate_spec_plots():
    # Configuration
    
    for metric in METRICS:
        plt.figure(figsize=(12, 6))
        
        # We collect all unique benchmarks across all files to keep the X-axis aligned
        all_benchmarks = set()
        
        # Plotting each device
        for folder, label in DEVICES.items():
            file_path = f"{DATA_DIR}/{folder}/{metric}.csv"
            
            if os.path.exists(file_path):
                df = pd.read_csv(file_path, sep='\t')
                df = df.sort_values(by="Benchmark")
                
                # Automatically find the ratio column (e.g., 'Ratio' or 'Peak_Ratio')
                ratio_col = [c for c in df.columns if 'Ratio' in c]
                bench_col = [c for c in df.columns if 'Bench' in c]

                if ratio_col and bench_col:
                    r_name = ratio_col[0]
                    b_name = bench_col[0]
                    
                    all_benchmarks.update(df[b_name].tolist())
                    
                    plt.plot(df[b_name], df[r_name], 
                             marker='o', 
                             label=label, 
                             color=COLORS[label], 
                             linewidth=2,
                             markersize=8)
                else:
                    print(f"Warning: Could not find Ratio/Benchmark columns in {file_path}")

        # Formatting
        title_formatted = metric.replace("_", " ").upper()
        plt.title(f"Comparison: {title_formatted} (Ratio)", fontsize=14)
        plt.ylabel("Ratio (More is Better)")
        plt.xlabel("Benchmarks")
        
        # Sort X-axis labels alphabetically for clarity
        plt.xticks(sorted(list(all_benchmarks)), rotation=45)
        
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.6)
        plt.tight_layout()
        
        # Save output
        save_name = f"{GRAPHICS_DIR}plot_{metric}.png"
        plt.savefig(save_name, dpi=300)
        print(f"Generated: {save_name}")
        plt.close()

if __name__ == "__main__":
    generate_spec_plots()