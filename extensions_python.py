"""
Some functions, that missing in Python
"""

from typing import Callable, Iterable, TypeAlias, TypeVar
from random import shuffle



char: TypeAlias = str

T = TypeVar("T")
R = TypeVar("R")



class UnreachableException(Exception):
    pass

def unreachable():
    raise UnreachableException("This code must be unreachable!")

def todo():
    raise NotImplementedError()

def assert_(b: bool, msg: str):
    assert(isinstance(b, bool))
    if b == False:
        raise AssertionError(msg)



def shuffled(l: list) -> list:
    l_copy = l.copy()
    shuffle(l_copy)
    return l_copy


def avg(l: list) -> float | None:
    if len(l) == 0:
        return None
    else:
        return sum(l)/len(l)


def flatten(l: list) -> list:
    res = []
    for el in l:
        if type(el) == list:
            res += flatten(el)
        else:
            res.append(el)
    return res


def join_lines(lines: Iterable[str]) -> str:
    return '\n'.join(lines)

def join_str(parts: Iterable[str]) -> str:
    return "".join(parts)

def join_elements(elements: Iterable[str]) -> str:
    return ", ".join(elements)


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


def to_str(smt: str | list[str]) -> str:
    # abc -> 'abc'
    # ['a', 'b'] -> ['a', 'b']
    match smt:
        case str(s):
            return "'" + s + "'"
        case list(l):
            return str(l)
        case None:
            return str(None)
        case _:
            unreachable()



def find_first(iterable: Iterable[T], f: Callable[[T], bool]) -> None | T:
    for el in iterable:
        if f(el) is True: # or `==`?
            return el
    else:
        return None

def find_all(iterable: Iterable[T], f: Callable[[T], bool]) -> None | list[T]:
    res: list[T] = [el for el in iterable if (f(el) == True)]
    return res if res else None



def enhance_enum(cls):
    assert(cls is not None)
    #TODO: assert: is Enum
    def get_by_index(index: int):
        assert(isinstance(index, int))
        assert(0 <= index < len(cls))
        return list(cls)[index]
    setattr(cls, "get_by_index", get_by_index)
    return cls


def beautiful_repr(cls):
    assert(cls is not None)
    def __repr__(self):
        return f"{type(self).__name__}" + "(" + join_elements([
            a + "=" + to_str(self.__getattribute__(a)) for a in self.__dict__
        ]) + ")"
    setattr(cls, "__repr__", __repr__)
    return cls


def is_latin(string: str | list[str]) -> bool:
    LATIN_LATTERS: str = "abcdefghijklmnopqrstuvwxyz"
    LATIN_PUNCTUATION: list[str] = [" ", ",", ".", "!", "?"]
    match string:
        case str(s):
            return all(map(
                lambda ch:
                    (ch in LATIN_LATTERS) or
                    (ch in LATIN_PUNCTUATION),
                s
            ))
        case list(l):
            return all(map(lambda s: is_latin(s), l))
        case _:
            unreachable()

