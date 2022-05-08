"""
Some functions, that missing in Python
"""

from typing import Callable, Iterable, TypeAlias
from random import shuffle



char: TypeAlias = str



class UnreachableException(Exception):
    pass

def unreachable():
    raise UnreachableException("This code must be unreachable!")

def todo():
    raise NotImplementedError()



def shuffled(l: list) -> list:
    l_copy = l.copy()
    shuffle(l_copy)
    return l_copy


def avg(l: list) -> float | None:
    if len(l) == 0:
        return None
    else:
        return sum(l)/len(l)


def join_lines(lines: Iterable[str]) -> str:
    return '\n'.join(lines)


def count_start(string: str, character: char=' ') -> int:
    for (i, c) in enumerate(string):
        if c != character:
            return i
    else:
        return len(string)


def map_by_line(function: Callable[[str], str], string: str) -> str:
    return join_lines(map(function, string.splitlines()))


def trim_by_first_line(string: str) -> str:
    string = join_lines(string.splitlines()[1:-1])
    first_line_shift = count_start(string.splitlines()[0])
    return map_by_line(lambda line: line[first_line_shift:], string)

