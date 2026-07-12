import numpy as np
import matplotlib.pyplot as plt

# 1. Simulation Parameters
NUM_AGENTS = 1000
STARTING_WEALTH = 100.0
SIM_STEPS = 100000 
POVERTY_LINE = 20.0  # Threshold where scarcity mindset kicks in

# 2. Initialize Population
agent_wealth = np.full(NUM_AGENTS, STARTING_WEALTH)

print("Running simulation with Scarcity + ROSCA Risk-Pooling...")

# 3. The Warped Transaction Loop
for step in range(SIM_STEPS):
    idx_a, idx_b = np.random.choice(NUM_AGENTS, size=2, replace=False)
    
    wealth_a = agent_wealth[idx_a]
    wealth_b = agent_wealth[idx_b]
    combined_wealth = wealth_a + wealth_b
    
    # Base case: completely random split
    split_percentage = np.random.random()
    
    # RULE 1: ROSCA Risk-Pooling Network
    # If BOTH agents are below the poverty line, they pool risk and split 50/50
    if wealth_a < POVERTY_LINE and wealth_b < POVERTY_LINE:
        split_percentage = 0.50
        
    # RULE 2: The Bandwidth Tax (Exploitation/Cognitive Load)
    # If Agent A is poor but Agent B is wealthy, Agent A gets a bad deal
    elif wealth_a < POVERTY_LINE and wealth_b >= POVERTY_LINE:
        split_percentage = np.random.uniform(0.0, 0.4) 
        
    # If Agent B is poor but Agent A is wealthy, Agent A keeps the advantage
    elif wealth_b < POVERTY_LINE and wealth_a >= POVERTY_LINE:
        split_percentage = np.random.uniform(0.6, 1.0)

    # Execute the trade/interaction
    agent_wealth[idx_a] = combined_wealth * split_percentage
    agent_wealth[idx_b] = combined_wealth * (1.0 - split_percentage)

print("Simulation finished! Generating final distribution graph...")

# 4. Plot the Results
plt.figure(figsize=(10, 6))
plt.plot(np.sort(agent_wealth), color='green', linewidth=2, label='Scarcity + ROSCA Networks')
plt.axhline(y=STARTING_WEALTH, color='red', linestyle='--', label='Initial Equal Distribution ($100)')
plt.axhline(y=POVERTY_LINE, color='orange', linestyle=':', label='Poverty Line ($20)')

plt.title('Econophysics Simulation: Structural Adaptation via Informal Architectures')
plt.xlabel('Agents (Sorted by Wealth)')
plt.ylabel('Wealth ($)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.show()