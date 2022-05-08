"""
Tests, Test Types, Test Lengths
"""

from dataclasses import dataclass
from enhance_enum import enhance_enum
from enum import Enum
from extensions import unreachable
from kana import KANA
from kanji import KANJI



@enhance_enum
class TestType(Enum):
    Hiragana = "Hiragana"
    Katakana = "Katakana"
    Kana = "Kana: Hiragana + Katakana"
    KanjiTranslate = "Kanji Translate"
    KanjiWrite = "Kanji Write"
    Kanji = "Kanji: Translation + Transliteration"
    Everything = "Everything: Kana + Kanji"


@enhance_enum
class TestLength(Enum):
    OnceEverySymbol = "Once every symbol"
    CertainAmount = "Certain amount"
    Endless = "Endless"


@dataclass
class Test:
    question: str
    answer: str | list[str]
    message_to_fmt: str
    user_answer: None | str = None

    def chech_answer(self, user_answer: str) -> bool:
        match self.answer:
            case str(correct_answer):
                return user_answer == correct_answer
            case list(correct_answers):
                return user_answer in correct_answers
            case _:
                unreachable()



def generate_tests(test_type: TestType) -> list[Test]:
    tests: list[Test] = []

    def generate_tests_for_hiragana() -> list[Test]:
        return [
            Test(
                letter.hiragana,
                letter.transliteration_to_latin,
                "Write {}"
            )
            for letter in KANA
        ]

    def generate_tests_for_katakana() -> list[Test]:
        return [
            Test(
                letter.katakana,
                letter.transliteration_to_latin,
                "Write {}"
            )
            for letter in KANA
        ]

    def generate_tests_for_kanji_translation() -> list[Test]:
        return [
            Test(
                kanji.symbol,
                kanji.translation_to_english,
                "Translate {}"
            )
            for kanji in KANJI
        ]

    def generate_tests_for_kanji_transliteration() -> list[Test]:
        return [
            Test(
                kanji.symbol,
                kanji.transliteration_to_latin,
                "Write {}"
            )
            for kanji in KANJI
        ]

    match test_type:
        case TestType.Hiragana:
            tests += generate_tests_for_hiragana()
        case TestType.Katakana:
            tests += generate_tests_for_katakana()
        case TestType.Kana:
            tests += generate_tests_for_hiragana()
            tests += generate_tests_for_katakana()
        case TestType.KanjiTranslate:
            tests += generate_tests_for_kanji_translation()
        case TestType.KanjiWrite:
            tests += generate_tests_for_kanji_transliteration()
        case TestType.Kanji:
            tests += generate_tests_for_kanji_translation()
            tests += generate_tests_for_kanji_transliteration()
        case TestType.Everything:
            tests += generate_tests_for_hiragana()
            tests += generate_tests_for_katakana()
            tests += generate_tests_for_kanji_translation()
            tests += generate_tests_for_kanji_transliteration()
        case _:
            unreachable()

    return tests

