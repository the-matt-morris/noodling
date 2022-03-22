import pytest

from project.utils import pythagorean


@pytest.mark.parametrize("x, y, expected", ((3, 4, 5), (6, 8, 10)))
def test_pythagorean(x: float, y: float, expected: float):
    """Test the pythagorean function

    Args:
        x (float): a float
        y (float): another float
        expected (float): expected result of pythagorean(x, y)
    """
    assert pythagorean(x, y) == expected
