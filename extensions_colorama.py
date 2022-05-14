"""
Extension for colorama
"""

from colorama import Style
from colorama import Fore as fg
#from colorama import Back as bg

RED = fg.RED
GREEN = fg.GREEN

def colorize(s: str, /, *, fg=None, bg=None) -> str:
    is_fg: bool = fg is not None
    is_bg: bool = bg is not None
    assert(is_fg or is_bg)
    return (
        (fg if is_fg else "") +
        (bg if is_bg else "") +
        s +
        (Style.RESET_ALL if (is_fg or is_bg) else "")
    )

