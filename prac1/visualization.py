import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set_style("white")


# ======================
# CPU DATA (each test = one bar)
# ======================
cpu_df = pd.DataFrame({
    "Label": [
        "Intel i5-12400 (Multi)",
        "Intel i5-12400 (Single)",
        "Ryzen 9 7900X (Multi)",
        "Ryzen 9 7900X (Single)",
        "Intel i5-13500 #1 (Multi)",
        "Intel i5-13500 #1 (Single)",
        "Intel i5-13500 #2 (Multi)",
        "Intel i5-13500 #2 (Single)",
    ],
    "Score": [
        12450, 2766,
        25602, 1629,
        13386, 1311,
        12926, 1334
    ],
    "Origin": [
        "Aula EPS 4", "Aula EPS 4",
        "Ordenador Personal", "Ordenador Personal",
        "Sala EPS1", "Sala EPS1",
        "Sala EPS1", "Sala EPS1"
    ]
})

# ======================
# GPU DATA (each test = one bar)
# ======================
gpu_df = pd.DataFrame({
    "Label": [
        "RTX 3050 #1 (Cinebench)",
        "RTX 3050 #1 (Unigine)",
        "RTX 3050 #2 (Cinebench)",
        "RTX 3050 #2 (Unigine)",
        "RTX 4070 Ti (Cinebench)",
        "RTX 4070 Ti (Unigine)",
    ],
    "Score": [
        4561, 2075,
        4599, 2039,
        18662, 5844
    ],
    "Origin": [
        "Sala EPS1", "Sala EPS1",
        "Sala EPS1", "Sala EPS1",
        "Ordenador Personal", "Ordenador Personal"
    ]
})

# ======================
# PLOTTING
# ======================
fig, axes = plt.subplots(2, 1, figsize=(14, 10))

# CPU

cpu_order = [
    "Intel i5-12400 (Single)",
    "Ryzen 9 7900X (Single)",
    "Intel i5-13500 #1 (Single)",
    "Intel i5-13500 #2 (Single)",
    "Intel i5-12400 (Multi)",
    "Ryzen 9 7900X (Multi)",
    "Intel i5-13500 #1 (Multi)",
    "Intel i5-13500 #2 (Multi)",
]
sns.barplot(
    data=cpu_df,
    x="Label",
    y="Score",
    hue="Origin",
    order=cpu_order,
    dodge=False,
    ax=axes[0]
)

axes[0].set_title("CPU Performance – Cinebench")
axes[0].set_ylabel("Score")
axes[0].set_xlabel("")
axes[0].tick_params(axis="x", rotation=20, labelsize=9)

# GPU plot
gpu_order = [
    "RTX 3050 #1 (Cinebench)",
    "RTX 3050 #2 (Cinebench)",
    "RTX 4070 Ti (Cinebench)",
    "RTX 3050 #1 (Unigine)",
    "RTX 3050 #2 (Unigine)",
    "RTX 4070 Ti (Unigine)",
]

sns.barplot(
    data=gpu_df,
    x="Label",
    y="Score",
    hue="Origin",
    order=gpu_order,
    dodge=False,
    ax=axes[1]
)

axes[1].set_title("GPU Performance – Cinebench & Unigine Heaven")
axes[1].set_ylabel("Score")
axes[1].set_xlabel("")
axes[1].tick_params(axis="x", rotation=20, labelsize=9)

plt.tight_layout()

# ======================
# SAVE
# ======================
plt.savefig("result.png", dpi=300, transparent=True)
plt.close()
