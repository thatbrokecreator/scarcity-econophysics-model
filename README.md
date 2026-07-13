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
## Results: Does ROSCA Risk-Pooling Actually Reduce Inequality?

To test whether the ROSCA mechanism meaningfully protects against the Bandwidth Tax
exploitation rule, I ran the simulation with and without ROSCA active, across a range
of poverty line thresholds, measuring the resulting Gini coefficient.

![ROSCA Comparison](results/scarcity_rosca_comparison.png)

**Finding: the ROSCA mechanism has little to no measurable effect on inequality** —
the Gini coefficient is nearly identical with and without it, across every poverty
line tested.

**Why:** I instrumented the simulation to count how often each rule actually fires.
Exploitation events (`poor_a_exploited` + `poor_b_exploited`) consistently outnumber
ROSCA-protected events by roughly 3–5x, even at high poverty lines. This is structural:
ROSCA only activates when *both* interacting agents happen to be poor — a joint
condition — while exploitation activates whenever *either* agent is poor. The
protective mechanism is triggered far less often than the exploitative one simply
because it requires a rarer coincidence, regardless of how favorable its terms are
when it does trigger.

**Implication:** a risk-pooling mechanism's real-world effectiveness depends not just
on how generous it is when used, but on how often it's actually invoked relative to
the harms it's meant to offset. A next step would be testing whether increasing
ROSCA participation likelihood (e.g., poor agents preferentially seeking out other
poor agents rather than meeting them randomly) closes this gap — which would mirror
how real ROSCAs work: by intentional membership, not random encounter.
