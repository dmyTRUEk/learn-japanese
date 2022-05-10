"""
Hiragana and Katakana letters class
"""

from dataclasses import dataclass

@dataclass
class JapaneseLetter:
    latin_spelling: str
    hiragana: str
    katakana: str

