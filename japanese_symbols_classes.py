# This is Japanese Letters and Kanji classes

from dataclasses import dataclass
from typing import TypeAlias



@dataclass
class JapaneseLetter:
    transliteration_to_latin: str
    hiragana: str
    katakana: str

@dataclass
class JapaneseKanji:
    symbol: str
    transliteration_to_latin: str | list[str]
    translation_to_english: str | list[str]

JapaneseSymbol: TypeAlias = JapaneseLetter | JapaneseKanji

