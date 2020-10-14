import pytest
from libs.math import add, sub


@pytest.mark.math
@pytest.mark.adding
@pytest.mark.parametrize("a", [1, 2, 3, 4])
def test_adding(random_int: int, a: int):
    expected = a + random_int
    assert add(a, random_int) == expected


@pytest.mark.math
@pytest.mark.subbing
@pytest.mark.parametrize("a, b, expected", [
    [1, 1, 0],
    [2, 1, 1],
    [3, 0, 3]
])
def test_sub(a: int, b: int, expected: int):
    assert sub(a, b) == expected
