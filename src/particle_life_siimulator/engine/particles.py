import numpy as np
from .config import SimulationConfig

class ParticleState:

    def __init__(self):
        self.position = np.array()
        self.velocity = np.array()
        self.type = np.array()

    def initialize_state(self):
        config = SimulationConfig()
        rng = np.random.default_rng(config.seed)
        self.position = rng.random(size=(config.num_particles, 2), dtype=np.float32)
        self.velocity = np.zeros(shape=(config.num_particles, 2), dtype= np.float32)
        self.type = rng.integers(0, config.num_types, size=config.num_particles)