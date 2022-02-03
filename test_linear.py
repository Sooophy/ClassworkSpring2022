import pytest


@pytest.mark.parametrize("tuple1, tuple2, input_x, expected", [
    ["1,1", "2,2", "3", 3],
    ["1,2", "2,4", "3", 6],
    ["1,3", "2,5", "3", 7],
    ])
def test_find_y(tuple1, tuple2, input_x, expected):
    from linear import find_y
    answer = find_y(tuple1, tuple2, input_x)
    assert answer == expected
