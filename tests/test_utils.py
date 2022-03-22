import inspect
import pytest
from typing import Any, Callable, List

from project.utils import pythagorean


def get_args(func: Callable[..., Any]) -> List[str]:
    return list(inspect.signature(func).parameters.keys())


@pytest.mark.parametrize("x, y, expected", ((3, 4, 5), (6, 8, 10)))
def test_pythagorean(x: float, y: float, expected: float):
    assert pythagorean(x, y) == expected
