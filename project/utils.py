import math


def pythagorean(x: float, y: float) -> float:
    """Pythagorean theorem (c**2 = sqrt(x**2 + y**2))

    Args:
        x (float): length of one side
        y (float): length of adjacent side

    Returns:
        float: length of hypotenuse
    """
    return math.sqrt(x**2 + y**2)
    