import tomllib
from pathlib import Path

DEFAULT_CONFIG_PATH = Path(__file__).resolve().parents[2] / "configs" / "default_config.toml"

class SimulationConfig():
    '''
    Stores constants for the simulation
    '''

    def __init__(
            self,
            num_particles=100,
            seed=45239,
            num_types=4
    ):
        self.num_particles = num_particles
        self.seed = seed
        self.num_types = num_types






def load_config(self, path=DEFAULT_CONFIG_PATH):
    '''
    Loads configuration from configs
    '''

    with path.open("rb") as f:
        config = tomllib.load(f)

        return SimulationConfig(
            **config["Simulation"]
        )