# Declaración directa de los datos
data_set_1 = [
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 83.9, "base_ratio": 1668, "marker": None},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 83.5, "base_ratio": 1677, "marker": "*"},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 83.4, "base_ratio": 1679, "marker": None},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 46.8, "base_ratio": 2993, "marker": None},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 46.3, "base_ratio": 3021, "marker": "*"},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 46.2, "base_ratio": 3033, "marker": None},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 22.7, "base_ratio": 4845, "marker": "*"},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 22.8, "base_ratio": 4826, "marker": None},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 22.6, "base_ratio": 4860, "marker": None},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 30.8, "base_ratio": 5842, "marker": "*"},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 30.8, "base_ratio": 5851, "marker": None},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 30.9, "base_ratio": 5828, "marker": None},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 26.6, "base_ratio": 3753, "marker": None},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 26.6, "base_ratio": 3763, "marker": "*"},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 26.5, "base_ratio": 3776, "marker": None},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 64.4, "base_ratio": 2797, "marker": None},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 63.2, "base_ratio": 2849, "marker": "*"},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 62.2, "base_ratio": 2892, "marker": None},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 22.6, "base_ratio": 5751, "marker": None},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 22.4, "base_ratio": 5804, "marker": "*"},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 22.2, "base_ratio": 5857, "marker": None},
    {"bench": "253.perlbmk", "base_ref": 1800, "base_run": None, "base_ratio": None, "marker": "X"},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 25.2, "base_ratio": 4357, "marker": None},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 24.1, "base_ratio": 4566, "marker": None},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 24.7, "base_ratio": 4446, "marker": "*"},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 30.1, "base_ratio": 6319, "marker": "*"},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 29.9, "base_ratio": 6359, "marker": None},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 30.1, "base_ratio": 6314, "marker": None},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 62.6, "base_ratio": 2395, "marker": "*"},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 62.5, "base_ratio": 2401, "marker": None},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 62.8, "base_ratio": 2387, "marker": None},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 72.5, "base_ratio": 4138, "marker": None},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 73.1, "base_ratio": 4104, "marker": "*"},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 73.6, "base_ratio": 4076, "marker": None},
]

# Creación del DataFrame
df1 = pl.DataFrame(data_set_1)

print(df1)