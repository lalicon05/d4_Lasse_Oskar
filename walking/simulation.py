"""
Authors:
Lasse Lindholm
Oskar Nerheim
"""

from walking.environment import Environment
from walking.alex import Alex



class Simulation:
    def __init__(self, alex: Alex, environment: Alex):
        self.alex = alex
        self.environment = environment