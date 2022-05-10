"""
Kanji or Word symbols class
"""

from extensions import find_all
from kana import JAPANESE_LETTERS



class JapaneseWord:
    symbol: str
    translation: str | list[str] # to english
    latin_spelling: str | list[str]
    kana_spelling: None | str | list[str] = None
    description: None | str = None

    def __init__(
            self,
            symbol: str,
            translation_to_english: str | list[str],
            /, *,
            ls: str | list[str], # latin spelling
            ks: None | str | list[str] = None, # kana spelling
            desc: None | str = None,
            ):
        self.symbol = symbol
        self.translation = translation_to_english
        self.kana_spelling = ks

        if (ks is not None) and (ls is None):
            latin_spelling = ""
            for letter in ks:
                lss = find_all(JAPANESE_LETTERS, lambda l: letter in [l.hiragana, l.katakana])
                assert(lss is not None)
                assert(len(lss) == 1)
                lss = lss[0]
                latin_spelling += lss.latin_spelling
            ls = latin_spelling

        self.latin_spelling = ls
        self.description = desc

