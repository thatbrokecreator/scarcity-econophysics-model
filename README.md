# Scarcity-Driven Econophysics Simulation
This project is an agent-based computational model that bridges statistical mechanics with behavioral finance. It simulates how wealth distributes across a population under standard thermodynamic conditions and explores how the system warps when introducing cognitive constraints and informal risk-pooling structures.
## Theoretical Framework
The simulation builds directly on the principles of econophysics, drawing an analogy between the kinetic theory of gases and the circulation of money:
* **The Physics Baseline:** In a closed system, gas molecules exchange kinetic energy through random collisions, naturally settling into a Boltzmann-Gibbs distribution. Here, individual economic agents exchange wealth through localized transactions. 
* **The Bandwidth Tax:** Moving beyond standard rational-actor models, the simulation implements a behavioral threshold (Poverty Line). When an agent's wealth drops below this line, their cognitive capacity is taxed due to environmental stress, skewing transaction dynamics against them.
* **Informal Architectures:** To simulate resilience, the model includes a defensive mechanism mimicking Rotating Savings and Credit Associations (ROSCAs). When two scarce agents interact, they leverage social collateral to split the transaction 50/50, flattening the steepness of the wealth distribution curve and creating a consumption-smoothing floor.
## Features
- **Agent-Based Modeling:** Tracks 1,000 distinct agents over 100,000 algorithmic transactions.
- **Asymmetric Transaction Dynamics:** Simulates the structural trapping of low-wealth cohorts.
- **Dynamic Visualization:** Generates real-time Matplotlib plots of final wealth distribution configurations compared against baseline asset averages.
## Installation & Execution
1. Clone or open the project workspace.
2. Install dependencies via the terminal:
   ```bash
   pip install numpy matplotlib

