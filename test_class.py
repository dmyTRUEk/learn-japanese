"""
Test class
"""

from random import choice as random_choice, gauss as random_gauss
from time import time as current_time
from typing import Iterator

from pipe import map
from pipe_extensions import abs_, max_, to_int

from extensions import join_str, unreachable
from kana import JAPANESE_LETTERS
from kana_class import JapaneseLetter
from kanji import JAPANESE_WORDS
from kanji_class import JapaneseWord
from test_type_enum import TestType



class Constants:
    SPELL_TO_FMT: str = "Spell {}"
    TRANSLATE_TO_FMT: str = "Translate {}"
    TIME_LIMIT: float = 0.1 # in seconds



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

    def __eq__(self, other: object) -> bool:
        if type(self) != type(other): return False
        assert(isinstance(other, Test))
        return (
            self._message_to_fmt == other._message_to_fmt and
            self._question == other._question and
            self.answer == other.answer and
            self.description == other.description
        )

    def __hash__(self) -> int:
        return hash(
            hash(self._message_to_fmt) +
            hash(self._question) +
            hash("".join(self.answer)) +
            hash(self.description)
        )

    def __repr__(self) -> str:
        return (
            "Test(" +
            f"_message_to_fmt='{self._message_to_fmt}'" + ", " +
            f"_question='{self._question}'" + ", " +
            (
                "answer=" +
                ("'" if isinstance(self.answer, str) else "") +
                str(self.answer) +
                ("'" if isinstance(self.answer, str) else "")
            ) + ", " +
            (
                "description=" +
                ("'" if isinstance(self.description, str) else "") +
                str(self.description) +
                ("'" if isinstance(self.description, str) else "")
            ) + ", " +
            (
                "user_answer=" +
                ("'" if isinstance(self.user_answer, str) else "") +
                str(self.user_answer) +
                ("'" if isinstance(self.user_answer, str) else "")
            ) +
            ")"
        )

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



def try_generate_unique_test(test_type: TestType, used_tests: set[Test]) -> None | Test:
    time_start = current_time()
    # TODO?: maybe optimize this by not checking time EVERY time, but once in 100 or smt?
    while (time_elapsed := current_time() - time_start) < Constants.TIME_LIMIT:
        test = generate_test(test_type)
        if test not in used_tests:
            used_tests.add(test)
            return test
    else:
        return None


def generate_tests_once(test_type: TestType) -> Iterator[Test]:
    used_tests: set[Test] = set()
    while (test := try_generate_unique_test(test_type, used_tests)) is not None:
        assert(test is not None)
        yield test

def generate_tests_certain_amount(test_type: TestType, n: int) -> Iterator[Test]:
    used_tests: set[Test] = set()
    for _ in range(n):
        test = try_generate_unique_test(test_type, used_tests)
        if test is None:
            used_tests = set()
            test = try_generate_unique_test(test_type, used_tests)
        assert(test is not None)
        yield test

def generate_tests_endless(test_type: TestType) -> Iterator[Test]:
    used_tests: set[Test] = set()
    while True:
        test = try_generate_unique_test(test_type, used_tests)
        if test is None:
            used_tests = set()
            test = try_generate_unique_test(test_type, used_tests)
        assert(test is not None)
        yield test



def gen_test_hiragana(japanese_letter: None | JapaneseLetter = None) -> Test:
    if japanese_letter is None:
        japanese_letter = random_choice(JAPANESE_LETTERS)
    return Test(
        Constants.SPELL_TO_FMT,
        japanese_letter.hiragana,
        japanese_letter.latin_spelling,
    )

def gen_test_katakana(japanese_letter: None | JapaneseLetter = None) -> Test:
    if japanese_letter is None:
        japanese_letter = random_choice(JAPANESE_LETTERS)
    return Test(
        Constants.SPELL_TO_FMT,
        japanese_letter.katakana,
        japanese_letter.latin_spelling,
    )

def gen_test_kanji_translate(japanese_word: None | JapaneseWord = None) -> Test:
    if japanese_word is None:
        japanese_word = random_choice(JAPANESE_WORDS)
    return Test(
        Constants.TRANSLATE_TO_FMT,
        japanese_word.symbol,
        japanese_word.translation,
        desc=japanese_word.description,
    )

def gen_test_kanji_spell(japanese_word: None | JapaneseWord = None) -> Test:
    if japanese_word is None:
        japanese_word = random_choice(JAPANESE_WORDS)
    return Test(
        Constants.SPELL_TO_FMT,
        japanese_word.symbol,
        japanese_word.latin_spelling,
        desc=japanese_word.description,
    )

def random_difficulty_by_gauss(difficulty: float) -> int:
    return random_gauss(difficulty, difficulty/2) | abs_ | to_int | max_(1)

def gen_test_hiragana_random_word(difficulty: float) -> Test:
    # TODO: extract this gauss to function
    n: int = random_difficulty_by_gauss(difficulty)
    # TODO: if n <= 0 => n=1
    letters: list[JapaneseLetter] = [random_choice(JAPANESE_LETTERS) for _ in range(n)]
    return Test(
        Constants.SPELL_TO_FMT,
        join_str(letters | map(lambda l: l.hiragana)),
        join_str(letters | map(lambda l: l.latin_spelling)),
    )

def gen_test_katakana_random_word(difficulty: float) -> Test:
    n: int = random_difficulty_by_gauss(difficulty)
    letters: list[JapaneseLetter] = [random_choice(JAPANESE_LETTERS) for _ in range(n)]
    return Test(
        Constants.SPELL_TO_FMT,
        join_str(letters | map(lambda l: l.katakana)),
        join_str(letters | map(lambda l: l.latin_spelling)),
    )



def generate_test(test_type: TestType) -> Test:
    match test_type:
        case TestType.Hiragana:
            return gen_test_hiragana()
        case TestType.Katakana:
            return gen_test_katakana()
        case TestType.Kana:
            return random_choice([
                gen_test_hiragana(),
                gen_test_katakana(),
            ])
        case TestType.KanaRandomWords:
            assert(hasattr(test_type, "difficulty"))
            return random_choice([
                gen_test_hiragana_random_word(test_type.difficulty),
                gen_test_katakana_random_word(test_type.difficulty),
            ])
        case TestType.KanjiTranslate:
            return gen_test_kanji_translate()
        case TestType.KanjiSpell:
            return gen_test_kanji_spell()
        case TestType.Kanji:
            return random_choice([
                gen_test_kanji_translate(),
                gen_test_kanji_spell(),
            ])
        case TestType.Everything:
            return random_choice([
                gen_test_hiragana(),
                gen_test_katakana(),
                gen_test_kanji_translate(),
                gen_test_kanji_spell(),
            ])
        case _:
            unreachable()
