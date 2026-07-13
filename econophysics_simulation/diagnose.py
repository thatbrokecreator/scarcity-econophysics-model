import numpy as np
from sweep_scarcity import run_scarcity_sim

def run_and_count(num_agents, sim_steps, poverty_line, seed):
    rng = np.random.default_rng(seed)
    agent_wealth = np.full(num_agents, 100.0)
    counts = {"rosca": 0, "poor_a_exploited": 0, "poor_b_exploited": 0, "random": 0}

    for step in range(sim_steps):
        idx_a, idx_b = rng.choice(num_agents, size=2, replace=False)
        wealth_a = agent_wealth[idx_a]
        wealth_b = agent_wealth[idx_b]
        combined_wealth = wealth_a + wealth_b
        split_percentage = rng.random()

        if wealth_a < poverty_line and wealth_b < poverty_line:
            split_percentage = 0.50
            counts["rosca"] += 1
        elif wealth_a < poverty_line and wealth_b >= poverty_line:
            split_percentage = rng.uniform(0.0, 0.4)
            counts["poor_a_exploited"] += 1
        elif wealth_b < poverty_line and wealth_a >= poverty_line:
            split_percentage = rng.uniform(0.6, 1.0)
            counts["poor_b_exploited"] += 1
        else:
            counts["random"] += 1

        agent_wealth[idx_a] = combined_wealth * split_percentage
        agent_wealth[idx_b] = combined_wealth * (1.0 - split_percentage)

    return counts

for pline in [10, 20, 30, 50]:
    counts = run_and_count(1000, 100_000, pline, seed=0)
    total = sum(counts.values())
    print(f"poverty_line={pline}: " + ", ".join(f"{k}={v/total*100:.1f}%" for k,v in counts.items()))