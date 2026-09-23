import pytest
from app.app import find_min, count_odds

# Test find_min with 3 different cases
@pytest.mark.parametrize("inputs, expected", [
    ([3, 1, 4, 2], 1),       # Case 1
    ([-5, 0, 10], -5),       # Case 2
    ([7], 7)                 # Case 3
])
def test_find_min(inputs, expected):
    assert find_min(inputs) == expected


# Test count_odds with 3 different cases
@pytest.mark.parametrize("inputs, expected", [
    ([1, 2, 3, 4, 5], 3),    # Case 1: Three odd numbers
    ([2, 4, 6], 0),          # Case 2: Zero odd numbers
    ([11, 13, 15], 3)        # Case 3: Three odd numbers
])
def test_count_odds(inputs, expected):
    assert count_odds(inputs) == expected
