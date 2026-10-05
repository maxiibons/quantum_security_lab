from enum import Enum
from random import Random


class Basis(str, Enum):
    """The two BB84 measurement bases: Z (rectilinear) and X (diagonal)."""

    Z = "Z"
    X = "X"


def measure_bit(
    prepared_bit: int,
    prepared_basis: Basis,
    measurement_basis: Basis,
    *,
    rng: Random,
) -> int:
    """Measure a BB84 bit in a basis and return the observed bit.

    Matching bases give the prepared bit with certainty. Different bases
    produce either result with equal probability.
    """
    if prepared_bit not in (0, 1):
        raise ValueError("prepared_bit must be 0 or 1")

    if prepared_basis == measurement_basis:
        return prepared_bit

    return rng.randint(0, 1)
