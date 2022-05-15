"""
Test Type enum
"""

from enum import Enum



class TestType(Enum):
    Hiragana = "Hiragana"
    Katakana = "Katakana"
    KanaRandomWords = "Kana words: generate random words"
    KanjiTranslate = "Kanji Translation"
    KanjiSpell = "Kanji Spelling"

