"""
Isolates the effect of the ROSCA risk-pooling rule by running the
scarcity model WITH and WITHOUT it, across a range of poverty line
thresholds, measuring the resulting Gini coefficient each time.
"""
import numpy as np

def run_scarcity_sim(num_agents, sim_steps, poverty_line, use_rosca, seed):
    rng = np.random.default_rng(seed)
    agent_wealth = np.full(num_agents, 100.0)

    for step in range(sim_steps):
        idx_a, idx_b = rng.choice(num_agents, size=2, replace=False)
        wealth_a = agent_wealth[idx_a]
        wealth_b = agent_wealth[idx_b]
        combined_wealth = wealth_a + wealth_b

        split_percentage = rng.random()

        if use_rosca and wealth_a < poverty_line and wealth_b < poverty_line:
            split_percentage = 0.50
        elif wealth_a < poverty_line and wealth_b >= poverty_line:
            split_percentage = rng.uniform(0.0, 0.4)
        elif wealth_b < poverty_line and wealth_a >= poverty_line:
            split_percentage = rng.uniform(0.6, 1.0)

        agent_wealth[idx_a] = combined_wealth * split_percentage
        agent_wealth[idx_b] = combined_wealth * (1.0 - split_percentage)

    return agent_wealth


def gini_coefficient(wealth):
    x = np.sort(wealth)
    n = len(x)
    cum = np.cumsum(x)
    return (n + 1 - 2 * np.sum(cum) / cum[-1]) / n


def frac_below(wealth, threshold):
    return np.mean(wealth < threshold)


if __name__ == "__main__":
    num_agents = 1000
    sim_steps = 100_000
    poverty_lines = [5, 10, 20, 30, 40, 50]
    trials = 5

    results = []
    for pline in poverty_lines:
        for use_rosca in [False, True]:
            ginis = []
            fracs = []
            for t in range(trials):
                w = run_scarcity_sim(num_agents, sim_steps, pline, use_rosca, seed=t)
                ginis.append(gini_coefficient(w))
                fracs.append(frac_below(w, pline))
            g_mean, g_std = np.mean(ginis), np.std(ginis)
            f_mean = np.mean(fracs)
            results.append((pline, use_rosca, g_mean, g_std, f_mean))
            label = "WITH ROSCA" if use_rosca else "NO ROSCA "
            print(f"poverty_line={pline:>3}  {label}  "
                  f"Gini={g_mean:.3f}+-{g_std:.3f}  "
                  f"frac_below_line={f_mean:.3f}")

    np.save("sweep_scarcity_results.npy", np.array(results))
    print("\nSaved to sweep_scarcity_results.npy")