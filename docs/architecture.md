# Architecture

---

## Simulation and Visualization
The simulation works independently from the visuals so that benchmarks and tets can run more specified only on the
engine.

### ParticleState
A class for storing the current state of all particles inlcuding their properties.

### Forces
Defines formulas for calculating different forces

### Interaction
Central part for calculating the next state for each step, calling definitions from forces and interaciton matrix.

### Simulation
Class for directing the simulation. Can call the next step of the simulation and can reset.

### Sinmulationconfig
Class for storing simulation parameters. Additionally loads in presets from configs.

---

![Architecture](docs/png/architecture.png)