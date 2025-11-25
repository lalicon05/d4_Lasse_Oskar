from walking.environment import Environment
from walking.simulation import Simulation


def test_run_once_reaches_kaia_and_counts_steps_and_seconds():
    env = Environment(aud_pos=50, pentagon_pos=30, kaia_pos=60)
    sim = Simulation(env)
    # deterministic walk east each second
    out = sim.run_once(step_chance=1.0, east_weight=1.0, p_kaia=1.0, p_pentagon=0.0)
    assert out == [60, 10, 10]


def test_run_once_reaches_pentagon():
    env = Environment(aud_pos=50, pentagon_pos=30, kaia_pos=60)
    sim = Simulation(env)
    # deterministic walk west to pentagon
    out = sim.run_once(step_chance=1.0, east_weight=0.0, p_kaia=0.0, p_pentagon=1.0)
    assert out == [30, 20, 20]