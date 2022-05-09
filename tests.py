"""
Tests, Test Types, Test Lengths
"""

from enhance_enum import enhance_enum
from enum import Enum
from extensions import unreachable
from kana import LETTERS
from kanji import WORDS



class Constants:
    TRANSLATE_TO_FMT: str = "Translate {}"
    SPELL_TO_FMT: str = "Spell {}"


@enhance_enum
class TestType(Enum):
    Hiragana = "Hiragana"
    Katakana = "Katakana"
    Kana = "Kana: Hiragana + Katakana"
    KanjiTranslate = "Kanji Translation"
    KanjiSpell = "Kanji Spelling"
    Kanji = "Kanji: Translation + Spelling"
    Everything = "Everything: Kana + Kanji"


@enhance_enum
class TestLength(Enum):
    OnceEverySymbol = "Once every symbol"
    CertainAmount = "Certain amount"
    Endless = "Endless"


class Test:
    _message_to_fmt: str
    _question: str
    answer: str | list[str]
    description: None | str = None
    user_answer: None | str = None

    def __init__(
            self,
            message_to_fmt: str,
            question: str,
            answer: str | list[str],
            /, *,
            desc: None | str = None
            ):
        self._message_to_fmt = message_to_fmt
        self._question = question
        self.answer = answer
        self.description = desc

    def get_message(self) -> str:
        return self._message_to_fmt.format(self._question)

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
                Constants.SPELL_TO_FMT,
                letter.hiragana,
                letter.latin_spelling,
            )
            for letter in LETTERS
        ]

    def generate_tests_for_katakana() -> list[Test]:
        return [
            Test(
                Constants.SPELL_TO_FMT,
                letter.katakana,
                letter.latin_spelling,
            )
            for letter in LETTERS
        ]

    def generate_tests_for_kanji_translation() -> list[Test]:
        return [
            Test(
                Constants.TRANSLATE_TO_FMT,
                kanji.symbol,
                kanji.translation,
            )
            for kanji in WORDS
        ]

    def generate_tests_for_kanji_transliteration() -> list[Test]:
        return [
            Test(
                Constants.SPELL_TO_FMT,
                kanji.symbol,
                kanji.latin_spelling,
            )
            for kanji in WORDS
            if kanji.latin_spelling is not None
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
        case TestType.KanjiSpell:
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

