"""
Unit Tests Class and Decorator
"""

from typing import Callable

from extensions_colorama import colorize, GREEN, RED



_TOTAL_TESTS: int = 0
_OK_TESTS   : int = 0
_ERROR_TESTS: int = 0


def unittest(f: Callable) -> Callable:
    assert(f is not None)
    global _ERROR_TESTS, _OK_TESTS, _TOTAL_TESTS
    _TOTAL_TESTS += 1
    try:
        f()
        print(colorize(f.__name__ + ": ok", fg=GREEN))
        _OK_TESTS += 1
    except AssertionError:
        _ERROR_TESTS += 1
        print(colorize(f.__name__ + ": ERROR", fg=RED))
    return f

