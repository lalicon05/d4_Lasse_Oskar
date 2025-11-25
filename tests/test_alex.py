import walking.alex as alex_module
from walking.alex import Alex


def test_try_step_direction_and_count():
    a = Alex(aud_pos=50, kaia_pos=60, pentagon_pos=30, step_chance=1.0, east_weight=1.0)
    assert a.pos == 50
    assert a.total_steps == 0

    a.try_step()
    assert a.pos == 51
    assert a.total_steps == 1

    b = Alex(aud_pos=50, kaia_pos=60, pentagon_pos=30, step_chance=1.0, east_weight=0.0)
    b.try_step()
    assert b.pos == 49
    assert b.total_steps == 1


def test_try_step_boundary_clamping():
    a = Alex(aud_pos=50, kaia_pos=60, pentagon_pos=30, step_chance=1.0, east_weight=1.0)
    a.pos = 100
    a.total_steps = 0
    a.try_step()
    assert a.pos == 100
    assert a.total_steps == 1

    b = Alex(aud_pos=50, kaia_pos=60, pentagon_pos=30, step_chance=1.0, east_weight=0.0)
    b.pos = 0
    b.total_steps = 0
    b.try_step()
    assert b.pos == 0
    assert b.total_steps == 1


def test_check_place_stop_with_monkeypatch(monkeypatch):
    a = Alex(aud_pos=50, kaia_pos=60, pentagon_pos=30, p_pentagon=0.5, p_kaia=0.5)

    monkeypatch.setattr(alex_module.random, "random", lambda: 0.0)
    a.pos = a.kaia_pos
    assert a.check_place_stop() is True
    
    a.pos = a.pent_pos
    assert a.check_place_stop() is True

    monkeypatch.setattr(alex_module.random, "random", lambda: 1.0)
    a.pos = a.kaia_pos
    assert a.check_place_stop() is False

    a.pos = a.pent_pos
    assert a.check_place_stop() is False