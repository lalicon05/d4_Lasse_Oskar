"""
students:
Lasse Lindholm
Oskar Nerheim
"""


from walking.environment import Environment
from walking.simulation import Simulation


if __name__ == "__main__":
    envi = Environment()
    sim = Simulation(envi)
    for i in range(100):
        print(sim.run_once())