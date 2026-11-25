import scipy
import numpy as np
from .config import SimulationConfig
from .particles import ParticleState

CONFIG = SimulationConfig()

def calculate_distance(particles: np.ndarray, index: int) -> np.ndarray:
    '''
    Helper function for calculating the distances from one point to every other one.
    The distance to the point itself is 0.
    :param particles: All particles
    :param index: Index of particle for calculating distance to
    :return: Array of distances to particle at index
    '''
    if particles.shape[1] != 2 or particles.shape[0] != CONFIG.num_particles:
        raise ValueError(f"particles expects shape (N, 2) but got {particles.shape}")

    difference = particles - particles[index]
    difference[index] = 0
    return np.linalg.norm(difference, axis=1)

def is_in_radius(distances: np.ndarray) -> np.ndarray:
    '''
    Helper function for checking if each particle is within the radius of influence.
    :param distances: Array of distances to a certain particle
    :return: Array of booleans
    '''
    return (distances > 0) & (CONFIG.influence_radius >= distances)


if __name__ == "__main__":
    rng = np.random.default_rng(12435)
    points = rng.normal(0, 100, size=(1000, 2))
    print(calculate_distance(points, 4))
    print(calculate_distance(points, 4).shape, points.shape)