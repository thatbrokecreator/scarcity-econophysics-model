"""
Tests a fix for the low ROSCA trigger-rate problem: instead of purely
random pairing, poor agents have some probability of specifically
seeking out another poor agent to transact with (mirroring how real
ROSCAs work through intentional membership, not random encounter).
"""
import numpy as np

def run_scarcity_sim_v2(num_agents, sim_steps, poverty_line, mode, seed,
                          rosca_seek_prob=0.5):
    rng = np.random.default_rng(seed)
    agent_wealth = np.full(num_agents, 100.0)

    for step in range(sim_steps):
        idx_a = rng.integers(num_agents)
        wealth_a = agent_wealth[idx_a]

        if mode == "preferential" and wealth_a < poverty_line and rng.random() < rosca_seek_prob:
            poor_indices = np.where(agent_wealth < poverty_line)[0]
            poor_indices = poor_indices[poor_indices != idx_a]
            if len(poor_indices) > 0:
                idx_b = rng.choice(poor_indices)
            else:
                idx_b = rng.integers(num_agents)
                while idx_b == idx_a:
                    idx_b = rng.integers(num_agents)
        else:
            idx_b = rng.integers(num_agents)
            while idx_b == idx_a:
                idx_b = rng.integers(num_agents)

        wealth_a = agent_wealth[idx_a]
        wealth_b = agent_wealth[idx_b]
        combined_wealth = wealth_a + wealth_b
        split_percentage = rng.random()

        if mode != "none" and wealth_a < poverty_line and wealth_b < poverty_line:
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


if __name__ == "__main__":
    num_agents = 1000
    sim_steps = 100_000
    poverty_line = 30
    trials = 5
    modes = ["none", "random", "preferential"]

    results = {}
    for mode in modes:
        ginis = []
        for t in range(trials):
            w = run_scarcity_sim_v2(num_agents, sim_steps, poverty_line, mode, seed=t)
            ginis.append(gini_coefficient(w))
        results[mode] = (np.mean(ginis), np.std(ginis))
        print(f"mode={mode:13s} Gini={np.mean(ginis):.3f} +- {np.std(ginis):.3f}")

    np.save("rosca_fix_results.npy", np.array([results[m] for m in modes]))