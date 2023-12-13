
from AOC5.main import seed_to_soil


def test_seed_to_soil():
    assert seed_to_soil(98) == 50
    assert seed_to_soil(99) == 51

test_seed_to_soil()