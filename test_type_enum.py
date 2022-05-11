"""
Test Type enum
"""

from enum import Enum

class TestType(Enum):
    Hiragana = "Hiragana"
    Katakana = "Katakana"
    Kana = "Kana: Hiragana + Katakana"
    KanaRandomWords = "Kana words: generate random words"
    KanjiTranslate = "Kanji Translation"
    KanjiSpell = "Kanji Spelling"
    Kanji = "Kanji: Translation + Spelling"
    Everything = "Everything: Kana + Kanji"

