"""
`pipe` lib extensions
"""

from pipe import Pipe, to_type



abs_ = Pipe(lambda x: abs(x))
min_ = lambda m: Pipe(lambda x: min(m, x))
max_ = lambda m: Pipe(lambda x: max(m, x))

to_str = to_type(str)
to_int = to_type(int)
to_float = to_type(float)

to_int_round = Pipe(lambda x: round(x))
