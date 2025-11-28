import walking.alex as alex_module
from walking.alex import Alex

"""
students:
Lasse Lindholm
Oskar Nerheim
"""


# a test to see that steps increase correctly and that directions are correct
def test_try_step_and_count():
    a = Alex(
                aud_pos=50,
                kaia_pos=60,
                pentagon_pos=30,
                step_chance=1.0,
                east_weight=1.0
            )

    assert a.pos == 50
    assert a.total_steps == 0

    a.try_step()
    assert a.pos == 51
    assert a.total_steps == 1

    b = Alex(
                aud_pos=50,
                kaia_pos=60,
                pentagon_pos=30,
                step_chance=1.0,
                east_weight=0.0
            )

    b.try_step()
    assert b.pos == 49
    assert b.total_steps == 1


# checks that the position cannot go outside the limits (0 and 100)
def test_boundaries():
    a = Alex(
                aud_pos=50,
                kaia_pos=60,
                pentagon_pos=30,
                step_chance=1.0,
                east_weight=1.0
            )

    a.pos = 100
    a.total_steps = 0
    a.try_step()
    assert a.pos == 100
    assert a.total_steps == 1

    b = Alex(
                aud_pos=50,
                kaia_pos=60,
                pentagon_pos=30,
                step_chance=1.0,
                east_weight=0.0
            )

    b.pos = 0
    b.total_steps = 0
    b.try_step()
    assert b.pos == 0
    assert b.total_steps == 1


# Checks that the stops at Kaia and Pentagon works correctly
# Using monkeypatch to force random number to be 'deterministick'
def test_check_place_stop(monkeypatch):
    a = Alex(
                aud_pos=50,
                kaia_pos=60,
                pentagon_pos=30,
                p_pentagon=0.5,
                p_kaia=0.5
            )

    # Guarantee that alex stops when placed at Kaia
    monkeypatch.setattr(alex_module.random, "random", lambda: 0.0)
    a.pos = a.kaia_pos
    assert a.check_place_stop() is True

    # Guarantee that Alex stops when placed at pentagon
    a.pos = a.pent_pos
    assert a.check_place_stop() is True

    # Guarantee that Alex desn't stop when at Kaia
    monkeypatch.setattr(alex_module.random, "random", lambda: 1.0)
    a.pos = a.kaia_pos
    assert a.check_place_stop() is False

    # Guarantee that Alex doesn't stop when at Pentagon
    a.pos = a.pent_pos
    assert a.check_place_stop() is False
