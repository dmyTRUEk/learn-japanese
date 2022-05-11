"""
Kanji or Word symbols class
"""

from pipe import all, map

from extensions_python import find_all, japanese_uppercase, unreachable
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
            ls: None | str | list[str] = None, # latin spelling
            ks: None | str | list[str] = None, # kana spelling
            desc: None | str = None,
            ):
        self.symbol = symbol
        self.translation = translation_to_english

        if ((symbol:=japanese_uppercase(symbol)) | all(lambda ch:
                (ch in JAPANESE_LETTERS | map(lambda l: l.hiragana)) or
                (ch in JAPANESE_LETTERS | map(lambda l: l.katakana))
                )):
            ks = symbol

        self.kana_spelling = ks

        if (ks is not None) and (ls is None):
            def kana_to_latin(kana_spelling: str) -> str:
                latin_spelling = ""
                for letter in kana_spelling:
                    lss = find_all(JAPANESE_LETTERS, lambda l: letter in [l.hiragana, l.katakana])
                    assert(lss is not None)
                    assert(len(lss) == 1)
                    lss = lss[0]
                    latin_spelling += lss.latin_spelling
                return latin_spelling

            match ks:
                case str(ks):
                    ls = kana_to_latin(ks)
                case list(kss):
                    ls = [kana_to_latin(ks) for ks in kss]
                case _:
                    unreachable()

        assert(ls is not None)
        self.latin_spelling = ls
        self.description = desc

