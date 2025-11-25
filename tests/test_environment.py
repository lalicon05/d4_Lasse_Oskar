from walking.environment import Environment


def test_environment_defaults():
    env = Environment()
    assert env.e6_pos == 0
    assert env.aud_pos == 50
    assert env.pentagon_pos == 30
    assert env.kaia_pos == 60
    assert env.train_pos == 100


def test_environment_custom_positions():
    env = Environment(e6_pos=1, aud_pos=5, pentagon_pos=8, kaia_pos=42, train_pos=99)
    assert env.e6_pos == 1
    assert env.aud_pos == 5
    assert env.pentagon_pos == 8
    assert env.kaia_pos == 42
    assert env.train_pos == 99