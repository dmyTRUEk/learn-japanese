"""
`pipe` lib extensions
"""

import builtins
from typing import Callable, Iterable

from pipe import Pipe

from extensions_python import flatten, T, R



abs_ = Pipe(lambda x: abs(x))
min_ = lambda m: Pipe(lambda x: min(m, x))
max_ = lambda m: Pipe(lambda x: max(m, x))

def to_type(t):
    return Pipe(lambda x: t(x))
to_str = to_type(str)
to_int = to_type(int)
to_float = to_type(float)
to_list = to_type(list)

to_int_round = Pipe(lambda x: round(x))

flatten_ = Pipe(lambda l: flatten(l))

@Pipe
def all_(iterable: Iterable[T], pred: Callable[[T], bool]):
    """Returns True if ALL elements in the given iterable are true for the
    given pred function"""
    return builtins.all(pred(x) for x in iterable)

@Pipe
def any_(iterable: Iterable[T], pred: Callable[[T], bool]):
    """Returns True if ANY element in the given iterable is True for the
    given pred function"""
    return builtins.any(pred(x) for x in iterable)

@Pipe
def map_(iterable: Iterable[T], selector: Callable[[T], R]) -> list[R]:
    return list(builtins.map(selector, iterable))

# TODO:
# @Pipe
# def filter_leave(iterable: Iterable[T], selector: Callable[[T], R]) -> list[R]:
#     return list(builtins.map(selector, iterable))
# @Pipe
# def filter_remove(iterable: Iterable[T], selector: Callable[[T], R]) -> list[R]:
#     return list(builtins.map(selector, iterable))

@Pipe
def uniq_(iterable: Iterable[T], key: Callable[[T], R]=lambda x: x) -> list[T]:
    """Deduplicate consecutive duplicate values."""
    iterator = iter(iterable)
    try:
        prev = next(iterator)
    except StopIteration:
        return []
    res = [prev]
    prevkey = key(prev)
    for item in iterator:
        itemkey = key(item)
        if itemkey != prevkey:
            res.append(item)
        prevkey = itemkey
    return res

