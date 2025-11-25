"""
students:
Lasse Lindholm
Oskar Nerheim
"""

class Environment:
    def __init__(self, e6_pos: int=0, aud_pos: int=50, pentagon_pos: int=30, kaia_pos: int=60, train_pos: int=100):
        """
        class containing locations from 0-100:
        """
        self.e6_pos = e6_pos
        self.aud_pos = aud_pos
        self.pentagon_pos = pentagon_pos
        self.kaia_pos = kaia_pos
        self.train_pos = train_pos
