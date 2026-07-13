import numpy as np
import matplotlib.pyplot as plt

results = np.load("sweep_scarcity_results.npy")
poverty_lines = sorted(set(results[:,0]))
no_rosca_gini = [results[(results[:,0]==p) & (results[:,1]==0)][0,2] for p in poverty_lines]
no_rosca_err  = [results[(results[:,0]==p) & (results[:,1]==0)][0,3] for p in poverty_lines]
with_rosca_gini = [results[(results[:,0]==p) & (results[:,1]==1)][0,2] for p in poverty_lines]
with_rosca_err  = [results[(results[:,0]==p) & (results[:,1]==1)][0,3] for p in poverty_lines]

fig, ax = plt.subplots(figsize=(8,5.5))
ax.errorbar(poverty_lines, no_rosca_gini, yerr=no_rosca_err, marker='o',
            label='No ROSCA (exploitation only)', color='crimson')
ax.errorbar(poverty_lines, with_rosca_gini, yerr=with_rosca_err, marker='s',
            label='With ROSCA risk-pooling', color='steelblue')
ax.set_xlabel("Poverty Line Threshold ($)")
ax.set_ylabel("Gini Coefficient")
ax.set_title("Does ROSCA Risk-Pooling Reduce Inequality?")
ax.legend()
ax.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("results/scarcity_rosca_comparison.png", dpi=150)
print("saved")