import polars as pl
import matplotlib.pyplot as plt

# Declaración directa de los datos
data_set_1 = [
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 83.9, "base_ratio": 1668},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 83.5, "base_ratio": 1677},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 83.4, "base_ratio": 1679},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 46.8, "base_ratio": 2993},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 46.3, "base_ratio": 3021},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 46.2, "base_ratio": 3033},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 22.7, "base_ratio": 4845},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 22.8, "base_ratio": 4826},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 22.6, "base_ratio": 4860},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 30.8, "base_ratio": 5842},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 30.8, "base_ratio": 5851},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 30.9, "base_ratio": 5828},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 26.6, "base_ratio": 3753},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 26.6, "base_ratio": 3763},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 26.5, "base_ratio": 3776},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 64.4, "base_ratio": 2797},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 63.2, "base_ratio": 2849},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 62.2, "base_ratio": 2892},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 22.6, "base_ratio": 5751},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 22.4, "base_ratio": 5804},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 22.2, "base_ratio": 5857},
    {"bench": "253.perlbmk", "base_ref": 1800, "base_run": None, "base_ratio": None},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 25.2, "base_ratio": 4357},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 24.1, "base_ratio": 4566},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 24.7, "base_ratio": 4446},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 30.1, "base_ratio": 6319},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 29.9, "base_ratio": 6359},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 30.1, "base_ratio": 6314},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 62.6, "base_ratio": 2395},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 62.5, "base_ratio": 2401},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 62.8, "base_ratio": 2387},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 72.5, "base_ratio": 4138},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 73.1, "base_ratio": 4104},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 73.6, "base_ratio": 4076},
]

# Declaración manual de los nuevos datos
data_set_2 = [
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 47.3, "base_ratio": 2961},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 46.9, "base_ratio": 2987},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 46.8, "base_ratio": 2989},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 26.7, "base_ratio": 5249},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 26.9, "base_ratio": 5208},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 26.8, "base_ratio": 5228},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 12.9, "base_ratio": 8507},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 12.9, "base_ratio": 8556},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 12.9, "base_ratio": 8528},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 17.8, "base_ratio": 10114},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 17.0, "base_ratio": 10565},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 17.0, "base_ratio": 10583},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 14.8, "base_ratio": 6746},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 14.7, "base_ratio": 6795},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 14.7, "base_ratio": 6783},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 34.9, "base_ratio": 5158},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 34.5, "base_ratio": 5225},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 34.4, "base_ratio": 5229},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 12.6, "base_ratio": 10297},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 12.9, "base_ratio": 10049},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 12.5, "base_ratio": 10374},
    {"bench": "253.perlbmk", "base_ref": 1800, "base_run": None, "base_ratio": None},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 14.7, "base_ratio": 7478},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 14.4, "base_ratio": 7640},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 14.5, "base_ratio": 7611},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 16.2, "base_ratio": 11705},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 16.3, "base_ratio": 11692},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 16.4, "base_ratio": 11614},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 34.5, "base_ratio": 4346},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 34.6, "base_ratio": 4336},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 34.5, "base_ratio": 4347},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 41.9, "base_ratio": 7158},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 41.4, "base_ratio": 7240},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 41.4, "base_ratio": 7245},
]

# Tercera tanda de datos declarada manualmente
data_set_3 = [
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 43.7, "base_ratio": 3204},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 43.8, "base_ratio": 3198},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 43.7, "base_ratio": 3204},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 26.0, "base_ratio": 5383},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 26.3, "base_ratio": 5315},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 25.8, "base_ratio": 5426},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 11.2, "base_ratio": 9850},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 11.2, "base_ratio": 9861},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 11.2, "base_ratio": 9824},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 12.7, "base_ratio": 14192},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 12.9, "base_ratio": 13953},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 12.9, "base_ratio": 14007},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 12.9, "base_ratio": 7776},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 12.8, "base_ratio": 7823},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 12.8, "base_ratio": 7815},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 31.0, "base_ratio": 5807},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 31.2, "base_ratio": 5764},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 31.4, "base_ratio": 5740},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 15.7, "base_ratio": 8292},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 15.7, "base_ratio": 8288},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 15.6, "base_ratio": 8325},
    {"bench": "253.perlbmk", "base_ref": 1800, "base_run": None, "base_ratio": None},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 13.0, "base_ratio": 8431},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 12.9, "base_ratio": 8507},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 13.0, "base_ratio": 8480},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 19.2, "base_ratio": 9887},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 19.3, "base_ratio": 9856},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 19.3, "base_ratio": 9858},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 29.3, "base_ratio": 5114},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 28.6, "base_ratio": 5239},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 28.9, "base_ratio": 5188},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 37.7, "base_ratio": 7951},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 38.0, "base_ratio": 7896},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 38.9, "base_ratio": 7718},
]

# 2. Creación de DataFrames y concatenación
df1 = pl.DataFrame(data_set_1).with_columns(pl.lit("Dispositivo 1").alias("device"))
df2 = pl.DataFrame(data_set_2).with_columns(pl.lit("Dispositivo 2").alias("device"))
df3 = pl.DataFrame(data_set_3).with_columns(pl.lit("Dispositivo 3").alias("device"))

# 1. Combinar los datos (asumiendo que df1, df2 y df3 ya están declarados)
all_data = pl.concat([df1, df2, df3])

# 2. Agrupar por Dispositivo y Benchmark para calcular la media
# Esto soluciona el problema de los nombres repetidos automáticamente
df_final = (
    all_data.group_by(["device", "bench"])
    .agg([
        pl.col("base_run").mean(),
        pl.col("base_ratio").mean()
    ])
    .sort("bench")
)

def save_clean_plot(column, title, ylabel, filename):
    plt.figure(figsize=(12, 6))
    colors = {"Dispositivo 1": "tab:blue", "Dispositivo 2": "tab:orange", "Dispositivo 3": "tab:green"}
    
    for dev in colors:
        # Filtramos por dispositivo
        subset = df_final.filter(pl.col("device") == dev).sort("bench")
        
        # Al haber agrupado, ahora 'subset' tiene exactamente una fila por benchmark
        plt.plot(subset["bench"], subset[column], marker='o', label=dev, color=colors[dev], linewidth=2)
    
    plt.title(title, fontsize=14)
    plt.ylabel(ylabel)
    plt.xlabel("Benchmark (Valores Promediados)")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()

# Guardar resultados
save_clean_plot("base_run", "Media de Base Run", "Segundos (Menos es mejor)", "media_base_run.png")
save_clean_plot("base_ratio", "Media de Base Ratio", "Ratio (Más es mejor)", "media_base_ratio.png")