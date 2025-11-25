"""
Authors:
Lasse Lindholm
Oskar Nerheim
"""

from walking.environment import Environment
from walking.alex import Alex


class Simulation:
    def __init__(self, environment: Environment):
        self.env = environment
    
    def run_once(self, step_chance: float =0.2, east_weight: float=0.5, p_pentagon: float=0.5,p_kaia: float =0.5):
        alex = Alex(
                aud_pos = self.env.aud_pos, 
                kaia_pos = self.env.kaia_pos, 
                pentagon_pos = self.env.pentagon_pos, 
                step_chance = step_chance, 
                east_weight = east_weight,
                p_kaia = p_kaia,
                p_pentagon = p_pentagon
                )
        seconds = 0

        while True:
            alex.try_step()
            seconds += 1

            if alex.check_place_stop():
                return [alex.pos, alex.total_steps, seconds]