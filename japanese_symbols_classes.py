"""
Kana and Kanji classes
"""

from dataclasses import dataclass
from typing import TypeAlias



@dataclass
class JapaneseLetter:
    latin_spelling: str
    hiragana: str
    katakana: str

class JapaneseWord:
    symbol: str
    translation: str | list[str] # to english
    kana_spelling: None | str | list[str] = None
    latin_spelling: None | str | list[str] = None
    description: None | str = None

    def __init__(
            self,
            symbol: str,
            translation_to_english: str | list[str],
            /, *,
            ks: None | str | list[str] = None, # kana spelling
            ls: None | str | list[str] = None, # latin spelling
            desc: None | str = None,
            ):
        self.symbol = symbol
        self.translation = translation_to_english
        self.kana_spelling = ks
        self.latin_spelling = ls
        self.description = desc



JapaneseSymbol: TypeAlias = JapaneseLetter | JapaneseWord

