import numpy as np
import matplotlib.pyplot as plt

data = np.load("rosca_fix_results.npy")
modes = ["No ROSCA", "ROSCA\n(random pairing)", "ROSCA\n(preferential pairing)"]
means = data[:,0]
errs = data[:,1]
colors = ['gray', 'steelblue', 'crimson']

fig, ax = plt.subplots(figsize=(7.5,5.5))
bars = ax.bar(modes, means, yerr=errs, color=colors, capsize=6)
ax.set_ylabel("Gini Coefficient")
ax.set_title("Does 'Fixing' ROSCA Matching Actually Help?\n(poverty_line=30)")
ax.set_ylim(0.45, 0.58)
ax.grid(axis='y', alpha=0.3)
for bar, mean in zip(bars, means):
    ax.text(bar.get_x()+bar.get_width()/2, mean+0.005, f"{mean:.3f}", ha='center')
plt.tight_layout()
plt.savefig("results/rosca_fix_comparison.png", dpi=150)
print("saved")