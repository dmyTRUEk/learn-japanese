"""
Some functions, that missing in Python
"""

from typing import Callable, Iterable, TypeAlias, TypeVar
from random import shuffle



char: TypeAlias = str

T = TypeVar("T")



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


def str_or_list_to_str(string: str | list[str]) -> str:
    # abc -> 'abc'
    # ['a', 'b'] -> ['a', 'b']
    return (
        ("'" if isinstance(string, str) else "") +
        str(string) +
        ("'" if isinstance(string, str) else "")
    )



def find_first(iterable: Iterable[T], f: Callable[[T], bool]) -> None | T:
    for el in iterable:
        if f(el) is True: # or maybe use `==`?
            return el
    else:
        return None

def find_all(iterable: Iterable[T], f: Callable[[T], bool]) -> None | list[T]:
    res: list[T] = [el for el in iterable if (f(el) == True)]
    return res if res else None



def enhance_enum(cls):
    assert(cls is not None)
    def get_by_index(index: int):
        assert(isinstance(index, int))
        assert(0 <= index < len(cls))
        return list(cls)[index]
    setattr(cls, "get_by_index", get_by_index)
    return cls



def japanese_uppercase(string: str):
    res = ""
    for ch in string:
        match ch:
            case 'ょ':
                res += 'よ'
            case _:
                res += ch
    return res

def beautiful_repr(cls):
    assert(cls is not None)
    def __repr__(self):
        return f"{type(self).__name__}" + "(" + join_elements([
            a + "=" + str_or_list_to_str(self.__getattribute__(a)) for a in self.__dict__
        ]) + ")"
    setattr(cls, "__repr__", __repr__)
    return cls

