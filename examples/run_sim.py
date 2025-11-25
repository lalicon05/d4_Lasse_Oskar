"""
students:
Lasse Lindholm
Oskar Nerheim
"""


from walking.environment import Environment
from walking.simulation import Simulation
from walking.alex import Alex


# Function to print results simulating automatically
def print_results(results: list):

    # The first variables are variables that are going to be added to
    kaia_results = []
    pent_results = []

    kaia_sec = 0
    pent_sec = 0

    kaia_step = 0
    pent_step = 0

    # sorts them to get average values for each one
    for result in results:
        if result[0] == "kaia":
            kaia_results.append(result)
            kaia_sec += result[2]
            kaia_step += result[1]
        elif result[0] == "pentagon":
            pent_results.append(result)
            pent_sec += result[2]
            pent_step += result[1]

    # calculates average time in seconds to get to both Kaia and Pentagon
    avg_kaia_sec = round(kaia_sec / len(kaia_results), 2)
    avg_pent_sec = round(pent_sec / len(pent_results), 2)

    # calculates average steps to get to both Kaia and Pentagon
    avg_kaia_step = round(kaia_step / len(kaia_results), 2)
    avg_pent_step = round(pent_step / len(pent_results), 2)

    # prints out the data
    print(f"Kaia ends: {len(kaia_results)}, Pentagon ends: {len(pent_results)}")
    print(f"avg kaia time: {avg_kaia_sec}, avg pent time: {avg_pent_sec}")
    print(f"avg kaia step: {avg_kaia_step}, avg pent step: {avg_pent_step}")


# runs the simulations 1000 times while prints information from the results
if __name__ == "__main__":
    envi = Environment()

    # make a sim object with default settings and simulate it 1000 times
    sim = Simulation(envi)
    result_1 = []
    for i in range(1000):
        result_1.append(sim.run_once())

    print_results(result_1)
