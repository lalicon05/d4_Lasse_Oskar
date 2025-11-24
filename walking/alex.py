"""
students:
Lasse Lindholm
Oskar Nerheim
"""
import random

class Alex:
    def __init__(self, aud_pos: int, kaia_pos: int, pentagon_pos:int, step_chance: float =0.2, east_weigth: float=0.5, p_pentagon: float=0.5,p_kaia: float =0.5):
        """
        simulates Alex walking from Aud Max to Kaia or Pentagon

        aud_pos (int): position of AudMax
        kaia_pos (int): position of Kaia
        pent_pos (int): position of Pentagon
        pos (int): current position of Alex
        total_steps (int): counter for steps

        step_chance (float), default 0.2: chance of stepping
        east_weight (float): chance of moving east
        p_pentagon (float): chance of staying at pentagon
        p_kaia (float): chance of staying at kaia
        """

        self.aud_pos = aud_pos
        self.kaia_pos = kaia_pos
        self.pent_pos = pentagon_pos
        self.pos = aud_pos
        self.total_steps = 0

        self.step_chance = step_chance
        self.east_weight = east_weigth

        self.p_pentagon = p_pentagon
        self.p_kaia = p_kaia

    
    def step(self):
        step_rng = random.random() # Gets a random float between 0 and 1

        if step_rng > self.step_chance: # Checks if Alex takes a step
            dir_rng = random.random()
            
            if dir_rng <= self.east_weight: # Checks which direction to move
                self.pos += 1
            else:
                self.pos -= 1
            
            self.pos = max(0, min(100, self.pos))
            self.total_steps += 1
    
    def check_place_stop(self):
        if self.pos == self.pent_pos:
            return random.random() < self.p_pentagon
        
        elif self.pos == self.kaia_pos:
            return random.random() < self.p_kaia