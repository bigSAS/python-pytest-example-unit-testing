import pytest
from random import randrange


@pytest.fixture(scope='function')
def random_int() -> int:
    """ Random int number from 0 to 100 """
    return randrange(0, 100)
