import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from math import pi

# 1. Load Data
df = pd.read_csv("outputs/tdd_full_dataset.csv")

# QECI Calculation for Pareto
max_time = df["Time (min)"].max()
min_time = df["Time (min)"].min()
max_mut = df["Mutation Score %"].max()
max_def = df["Defects"].max()

def calc_qeci(row):
    e_norm = (max_time - row["Time (min)"]) / (max_time - min_time)
    q_norm = 0.5 * ((row["Mutation Score %"] / max_mut) + ((max_def - row["Defects"]) / max_def))
    return (0.6 * q_norm) + (0.4 * e_norm)

df["QECI"] = df.apply(calc_qeci, axis=1)

# Agregate data
agg = df.groupby("Mode").agg({
    "Time (min)": ["mean", "std"],
    "Tests": ["mean", "std"],
    "Assert": ["mean", "std"],
    "Iter": ["mean", "std"],
    "Coverage %": ["mean", "std"],
    "Mutation Score %": ["mean", "std"],
    "Defects": ["mean", "std"],
    "Cog Load": ["mean", "std"],
    "QECI": ["mean"]
}).reindex(["Manual", "AI-TDD", "Hybrid"])

# Flatten MultiIndex columns
agg.columns = ['_'.join(col).strip() for col in agg.columns.values]

# --- FIGURE II: Classified Data (Bar Chart) with Error Bars ---
plt.style.use('default')
fig2, ax2 = plt.subplots(figsize=(10, 6), dpi=300)

modes = agg.index
metrics_mean = ["Time (min)_mean", "Tests_mean", "Assert_mean", "Iter_mean"]
metrics_std = ["Time (min)_std", "Tests_std", "Assert_std", "Iter_std"]
labels = ["Time (min)", "Mean Tests", "Mean Assertions", "Mean Iterations"]
colors = ['#4A6990', '#7A9A8C', '#E6A57E', '#A68BA1']

x = np.arange(len(modes))
width = 0.2

for i, (metric_m, metric_s) in enumerate(zip(metrics_mean, metrics_std)):
    vals = agg[metric_m]
    stds = agg[metric_s]
    # Calculate 95% CI: 1.96 * std / sqrt(n) where n=10
    ci = 1.96 * stds / np.sqrt(10)
    
    rects = ax2.bar(x + i*width - width*1.5, vals, width, yerr=ci, capsize=4, 
                    label=labels[i], color=colors[i], edgecolor='white', alpha=0.9,
                    error_kw=dict(ecolor='gray', lw=1.5, capsize=3, capthick=1.5))
    
    # Add value labels
    for rect in rects:
        height = rect.get_height()
        ax2.annotate(f'{height:.1f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 15), # offset to avoid overlapping with error bar
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=9, fontweight='bold')

ax2.set_ylabel('Value (Count / Minutes)', fontsize=12)
ax2.set_title('FIGURE II \u2014 Classified Data (Manual and AI) with 95% CI', fontsize=14, pad=20, fontweight='bold')
ax2.set_xticks(x)
ax2.set_xticklabels(modes, fontsize=12)
ax2.legend(loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=4, frameon=False, fontsize=10)
ax2.yaxis.grid(True, linestyle='--', alpha=0.7)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig("outputs/figure_2_classified_data.png", dpi=300)
plt.close()

# --- FIGURE III: Quality Efficiency Matrix (Radar Chart) ---
def make_radar_chart():
    radar_data = {}
    for mode in modes:
        radar_data[mode] = [
            agg.loc[mode, "Coverage %_mean"],
            agg.loc[mode, "Mutation Score %_mean"],
            (10 - agg.loc[mode, "Defects_mean"]) * 10,
            (agg.loc[mode, "Tests_mean"] / 10) * 100,
            (1 - (agg.loc[mode, "Time (min)_mean"] / 60)) * 100,
            (10 - agg.loc[mode, "Cog Load_mean"]) * 10
        ]
    
    categories = ['Coverage %', 'Mutation Score %', 'Defect-Free', 'Test Completeness', 'Speed Score', 'Low Cog Load']
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    fig3, ax3 = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True), dpi=300)
    colors_radar = {'Manual': '#4A6990', 'AI-TDD': '#7A9A8C', 'Hybrid': '#E6A57E'}
    
    for mode, values in radar_data.items():
        values += values[:1]
        ax3.plot(angles, values, linewidth=2, linestyle='solid', label=mode, color=colors_radar[mode])
        ax3.fill(angles, values, color=colors_radar[mode], alpha=0.25)
    
    plt.xticks(angles[:-1], categories, size=11, fontweight='bold')
    ax3.set_rlabel_position(30)
    plt.yticks([20, 40, 60, 80, 100], ["20", "40", "60", "80", "100"], color="grey", size=8)
    plt.ylim(0, 100)
    
    plt.title('FIGURE III \u2014 Comparative Analysis of Software Quality\nand Efficiency Matrix', size=14, fontweight='bold', pad=30)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1), frameon=True)
    
    plt.savefig("outputs/figure_3_quality_efficiency_matrix.png", dpi=300, bbox_inches='tight')
    plt.close()

make_radar_chart()

# --- FIGURE IV: Mutation vs Coverage Scatterplot ---
fig4, ax4 = plt.subplots(figsize=(8, 6), dpi=300)
colors_scatter = {'Manual': '#4A6990', 'AI-TDD': '#7A9A8C', 'Hybrid': '#E6A57E'}

for mode in modes:
    subset = df[df['Mode'] == mode]
    ax4.scatter(subset['Coverage %'], subset['Mutation Score %'], 
                label=mode, color=colors_scatter[mode], s=80, alpha=0.8, edgecolor='w')

# Plot means as larger stars
for mode in modes:
    ax4.scatter(agg.loc[mode, 'Coverage %_mean'], agg.loc[mode, 'Mutation Score %_mean'], 
                color=colors_scatter[mode], s=300, marker='*', edgecolor='black', zorder=5)

ax4.set_xlabel('Coverage (%)', fontsize=12, fontweight='bold')
ax4.set_ylabel('Mutation Score (%)', fontsize=12, fontweight='bold')
ax4.set_title('FIGURE IV \u2014 Mutation Score vs Coverage (The "Shallow Oracle" Effect)', fontsize=14, fontweight='bold')
ax4.legend(title='TDD Mode', frameon=True)
ax4.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig("outputs/figure_4_mutation_coverage.png", dpi=300)
plt.close()

# --- FIGURE V: Quality-Efficiency Pareto Frontier ---
fig5, ax5 = plt.subplots(figsize=(8, 6), dpi=300)

for mode in modes:
    ax5.scatter(agg.loc[mode, 'Time (min)_mean'], agg.loc[mode, 'QECI_mean'], 
                label=mode, color=colors_scatter[mode], s=150, zorder=3)

# Draw Pareto line connecting optimal points (AI-TDD for speed, Hybrid for QECI)
# Manual is sub-optimal in both compared to Hybrid.
pareto_x = [agg.loc['AI-TDD', 'Time (min)_mean'], agg.loc['Hybrid', 'Time (min)_mean']]
pareto_y = [agg.loc['AI-TDD', 'QECI_mean'], agg.loc['Hybrid', 'QECI_mean']]
ax5.plot(pareto_x, pareto_y, 'k--', alpha=0.5, label='Pareto Frontier', zorder=2)

ax5.set_xlabel('Mean Development Time (minutes) \u2190 Better', fontsize=12, fontweight='bold')
ax5.set_ylabel('Quality-Efficiency Composite Index (QECI) \u2191 Better', fontsize=12, fontweight='bold')
ax5.set_title('FIGURE V \u2014 Quality-Efficiency Pareto Frontier', fontsize=14, fontweight='bold')
ax5.legend(frameon=True)
ax5.grid(True, linestyle='--', alpha=0.5)
ax5.invert_xaxis() # Invert X so "better" (faster) is on the right

# Annotate points
for mode in modes:
    ax5.annotate(mode, 
                 (agg.loc[mode, 'Time (min)_mean'], agg.loc[mode, 'QECI_mean']),
                 xytext=(10, 10), textcoords='offset points', fontweight='bold')

plt.tight_layout()
plt.savefig("outputs/figure_5_qeci_pareto.png", dpi=300)
plt.close()

print("All figures (including new scatter and Pareto plots) generated successfully.")
