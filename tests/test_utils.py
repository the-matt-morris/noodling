import inspect
import functools
import pytest
from typing import Any, Callable, Iterable, List

from project.utils import pythagorean


def get_args(func: Callable[..., Any]) -> List[str]:
    return list(inspect.signature(func).parameters.keys())


def is_equal(func: Callable[..., Any], inputs: Iterable[Any]):
    func_args = get_args(func) + ["expected"]
    
    @functools.wraps(func)
    def wrapper(*args):
        assert func(*args[:-1]) == inputs[-1]
    
    sig = inspect.signature(func)
    sig = sig.replace(
        parameters=[
            inspect.Parameter(x, kind=inspect.Parameter.POSITIONAL_OR_KEYWORD)
            for x in func_args
        ],
        return_annotation=None,
    )
    
    wrapper.__signature__ = sig
    return pytest.mark.parametrize(",".join(func_args), inputs)(wrapper)


class TestUtils:

    test_pythagorean = is_equal(pythagorean, ((3, 4, 5), (6, 8, 10)))
