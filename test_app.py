import pytest
from app.app import find_min, count_odds


@pytest.mark.parametrize("inputs, expected", [
    ([3, 1, 4, 2], 1),       
    ([-5, 0, 10], -5),       
    ([7], 7)                 
])
def test_find_min(inputs, expected):
    assert find_min(inputs) == expected



@pytest.mark.parametrize("inputs, expected", [
    ([1, 2, 3, 4, 5], 3),    
    ([2, 4, 6], 0),          
    ([11, 13, 15], 3)        
])
def test_count_odds(inputs, expected):
    assert count_odds(inputs) == expected
