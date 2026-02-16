import polars as pl

# Declaración manual de los nuevos datos
data_set_2 = [
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 47.3, "base_ratio": 2961, "marker": None},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 46.9, "base_ratio": 2987, "marker": "*"},
    {"bench": "164.gzip", "base_ref": 1400, "base_run": 46.8, "base_ratio": 2989, "marker": None},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 26.7, "base_ratio": 5249, "marker": None},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 26.9, "base_ratio": 5208, "marker": None},
    {"bench": "175.vpr", "base_ref": 1400, "base_run": 26.8, "base_ratio": 5228, "marker": "*"},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 12.9, "base_ratio": 8507, "marker": None},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 12.9, "base_ratio": 8556, "marker": None},
    {"bench": "176.gcc", "base_ref": 1100, "base_run": 12.9, "base_ratio": 8528, "marker": "*"},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 17.8, "base_ratio": 10114, "marker": None},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 17.0, "base_ratio": 10565, "marker": "*"},
    {"bench": "181.mcf", "base_ref": 1800, "base_run": 17.0, "base_ratio": 10583, "marker": None},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 14.8, "base_ratio": 6746, "marker": None},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 14.7, "base_ratio": 6795, "marker": None},
    {"bench": "186.crafty", "base_ref": 1000, "base_run": 14.7, "base_ratio": 6783, "marker": "*"},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 34.9, "base_ratio": 5158, "marker": None},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 34.5, "base_ratio": 5225, "marker": "*"},
    {"bench": "197.parser", "base_ref": 1800, "base_run": 34.4, "base_ratio": 5229, "marker": None},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 12.6, "base_ratio": 10297, "marker": "*"},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 12.9, "base_ratio": 10049, "marker": None},
    {"bench": "252.eon", "base_ref": 1300, "base_run": 12.5, "base_ratio": 10374, "marker": None},
    {"bench": "253.perlbmk", "base_ref": 1800, "base_run": None, "base_ratio": None, "marker": "X"},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 14.7, "base_ratio": 7478, "marker": None},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 14.4, "base_ratio": 7640, "marker": None},
    {"bench": "254.gap", "base_ref": 1100, "base_run": 14.5, "base_ratio": 7611, "marker": "*"},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 16.2, "base_ratio": 11705, "marker": None},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 16.3, "base_ratio": 11692, "marker": "*"},
    {"bench": "255.vortex", "base_ref": 1900, "base_run": 16.4, "base_ratio": 11614, "marker": None},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 34.5, "base_ratio": 4346, "marker": "*"},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 34.6, "base_ratio": 4336, "marker": None},
    {"bench": "256.bzip2", "base_ref": 1500, "base_run": 34.5, "base_ratio": 4347, "marker": None},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 41.9, "base_ratio": 7158, "marker": None},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 41.4, "base_ratio": 7240, "marker": "*"},
    {"bench": "300.twolf", "base_ref": 3000, "base_run": 41.4, "base_ratio": 7245, "marker": None},
]

df2 = pl.DataFrame(data_set_2)

print(df2)