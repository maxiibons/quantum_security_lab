from random import Random

from qsl.quantum.measurement import Basis, measure_bit


def test_matching_basis_returns_prepared_bit():
    assert measure_bit(0, Basis.Z, Basis.Z, rng=Random(1)) == 0
    assert measure_bit(1, Basis.X, Basis.X, rng=Random(1)) == 1


def test_different_basis_gives_roughly_equal_outcomes():
    rng = Random(42)

    outcomes = [
        measure_bit(0, Basis.Z, Basis.X, rng=rng)
        for _ in range(1_000)
    ]

    ones = sum(outcomes)
    assert 400 < ones < 600


def test_invalid_prepared_bit_is_rejected():
    try:
        measure_bit(2, Basis.Z, Basis.Z, rng=Random(1))
    except ValueError:
        pass
    else:
        raise AssertionError("Expected invalid bit to raise ValueError")
