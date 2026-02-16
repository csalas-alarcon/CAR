import polars as pl

# Tercera tanda de datos declarada manualmente
data_set_3 = [
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 43.7, "base_ratio": 3204, "marker": "*"},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 43.8, "base_ratio": 3198, "marker": None},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 43.7, "base_ratio": 3204, "marker": None},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 26.0, "base_ratio": 5383, "marker": "*"},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 26.3, "base_ratio": 5315, "marker": None},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 25.8, "base_ratio": 5426, "marker": None},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 11.2, "base_ratio": 9850, "marker": "*"},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 11.2, "base_ratio": 9861, "marker": None},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 11.2, "base_ratio": 9824, "marker": None},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 12.7, "base_ratio": 14192, "marker": None},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 12.9, "base_ratio": 13953, "marker": None},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 12.9, "base_ratio": 14007, "marker": "*"},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 12.9, "base_ratio": 7776, "marker": None},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 12.8, "base_ratio": 7823, "marker": None},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 12.8, "base_ratio": 7815, "marker": "*"},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 31.0, "base_ratio": 5807, "marker": None},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 31.2, "base_ratio": 5764, "marker": "*"},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 31.4, "base_ratio": 5740, "marker": None},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 15.7, "base_ratio": 8292, "marker": "*"},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 15.7, "base_ratio": 8288, "marker": None},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 15.6, "base_ratio": 8325, "marker": None},
    {"bench": "253.perlbmk", "base_ref": 1800, "base_run": None, "base_ratio": None, "marker": "X"},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 13.0, "base_ratio": 8431, "marker": None},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 12.9, "base_ratio": 8507, "marker": None},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 13.0, "base_ratio": 8480, "marker": "*"},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 19.2, "base_ratio": 9887, "marker": None},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 19.3, "base_ratio": 9856, "marker": None},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 19.3, "base_ratio": 9858, "marker": "*"},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 29.3, "base_ratio": 5114, "marker": None},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 28.6, "base_ratio": 5239, "marker": None},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 28.9, "base_ratio": 5188, "marker": "*"},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 37.7, "base_ratio": 7951, "marker": None},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 38.0, "base_ratio": 7896, "marker": "*"},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 38.9, "base_ratio": 7718, "marker": None},
]

df3 = pl.DataFrame(data_set_3)

print(df3)