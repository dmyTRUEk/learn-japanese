"""
Tests generation
"""

from random import choice as random_choice, gauss as random_gauss
from time import time as current_time
from typing import Iterator

from extensions_python import join_str, unreachable
from extensions_pipe import abs_, map_, max_, to_int_round
from kana import JAPANESE_LETTERS
from kana_class import JapaneseLetter
from kanji import JAPANESE_WORDS
from kanji_class import JapaneseWord
from test_class import Test
from test_type_enum import TestType



class Constants:
    SPELL_TO_FMT: str = "Spell {}"
    TRANSLATE_TO_FMT: str = "Translate {}"
    TIME_LIMIT: float = 0.1 # in seconds
    DIFFICULTY_DEFAULT = 3



def try_generate_unique_test(test_types: list[TestType], used_tests: set[Test]) -> None | Test:
    time_start = current_time()
    # TODO?: maybe optimize this by not checking time EVERY time, but once in 100 or smt?
    while (time_elapsed := current_time() - time_start) < Constants.TIME_LIMIT:
        test = generate_test(test_types)
        if test not in used_tests:
            used_tests.add(test)
            return test
    else:
        return None


def generate_tests_once(test_types: list[TestType]) -> Iterator[Test]:
    used_tests: set[Test] = set()
    while (test := try_generate_unique_test(test_types, used_tests)) is not None:
        assert(test is not None)
        yield test

def generate_tests_certain_amount(test_types: list[TestType], n: int) -> Iterator[Test]:
    used_tests: set[Test] = set()
    for _ in range(n):
        test = try_generate_unique_test(test_types, used_tests)
        if test is None:
            used_tests = set()
            test = try_generate_unique_test(test_types, used_tests)
        assert(test is not None)
        yield test

def generate_tests_endless(test_types: list[TestType]) -> Iterator[Test]:
    used_tests: set[Test] = set()
    while True:
        test = try_generate_unique_test(test_types, used_tests)
        if test is None:
            used_tests = set()
            test = try_generate_unique_test(test_types, used_tests)
        assert(test is not None)
        yield test



def gen_test_hiragana(japanese_letter: None | JapaneseLetter = None) -> Test:
    if japanese_letter is None:
        assert(len(JAPANESE_LETTERS) > 0)
        japanese_letter = random_choice(JAPANESE_LETTERS)
    return Test(
        Constants.SPELL_TO_FMT,
        japanese_letter.hiragana,
        japanese_letter.latin_spelling,
    )

def gen_test_katakana(japanese_letter: None | JapaneseLetter = None) -> Test:
    if japanese_letter is None:
        assert(len(JAPANESE_LETTERS) > 0)
        japanese_letter = random_choice(JAPANESE_LETTERS)
    return Test(
        Constants.SPELL_TO_FMT,
        japanese_letter.katakana,
        japanese_letter.latin_spelling,
    )

def gen_test_kanji_translate(japanese_word: None | JapaneseWord = None) -> Test:
    if japanese_word is None:
        assert(len(JAPANESE_WORDS) > 0)
        japanese_word = random_choice(JAPANESE_WORDS)
    return Test(
        Constants.TRANSLATE_TO_FMT,
        japanese_word.word,
        japanese_word.translation,
        desc=japanese_word.description,
    )

def gen_test_kanji_spell(japanese_word: None | JapaneseWord = None) -> Test:
    if japanese_word is None:
        assert(len(JAPANESE_WORDS) > 0)
        while True:
            japanese_word = random_choice(JAPANESE_WORDS)
            if japanese_word.latin_spelling != None:
                break
    return Test(
        Constants.SPELL_TO_FMT,
        japanese_word.word,
        japanese_word.latin_spelling,
        desc=japanese_word.description,
    )

def random_difficulty_by_gauss(difficulty: float) -> int:
    return random_gauss(difficulty, difficulty/3) | abs_ | to_int_round | max_(1)

def gen_test_hiragana_random_word(difficulty: float) -> Test:
    assert(len(JAPANESE_LETTERS) > 0)
    n: int = random_difficulty_by_gauss(difficulty)
    letters: list[JapaneseLetter] = [random_choice(JAPANESE_LETTERS) for _ in range(n)]
    return Test(
        Constants.SPELL_TO_FMT,
        join_str(letters | map_(lambda l: l.hiragana)),
        join_str(letters | map_(lambda l: l.latin_spelling)),
    )

def gen_test_katakana_random_word(difficulty: float) -> Test:
    assert(len(JAPANESE_LETTERS) > 0)
    n: int = random_difficulty_by_gauss(difficulty)
    letters: list[JapaneseLetter] = [random_choice(JAPANESE_LETTERS) for _ in range(n)]
    return Test(
        Constants.SPELL_TO_FMT,
        join_str(letters | map_(lambda l: l.katakana)),
        join_str(letters | map_(lambda l: l.latin_spelling)),
    )



def generate_test(test_types: list[TestType]) -> Test:
    test_type: TestType = random_choice(test_types)
    match test_type:
        case TestType.Hiragana:
            return gen_test_hiragana()
        case TestType.Katakana:
            return gen_test_katakana()
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
        case _:
            unreachable()

