"""
Example script to run a single simulation of Alex walking home.
"""
from walking.simulation import Simulation
from walking.environment import Environment
from walking.alex import Alex

def main():
    # Set up environment: positions 0..100, with key locations
    env = Environment(length=100, pentagon_pos=10, audmax_pos=50, kaia_pos=90)

    # Create Alex with some probabilities
    alex = Alex(env, p_pentagon=0.7, p_kaia=0.6)

    # Run a single simulation until Alex reaches a dorm
    sim = Simulation(alex)
    sim.run()

    print(f"Alex ended up at {alex.position}")
    print(f"Total steps taken: {alex.steps}")
    print(f"Total seconds elapsed: {sim.time_elapsed}")

if __name__ == "__main__":
    main()
