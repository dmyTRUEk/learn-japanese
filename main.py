# Learn Japanese program by dmyTRUEk

__version__ = "0.1.0"

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Iterable, TypeAlias

import random



char: TypeAlias = str

class Constants:
    STOP_SEQ: str = "exit"



class UnreachableException(Exception): pass
def unreachable(): raise UnreachableException("This code must be unreachable!")
def todo(): raise NotImplementedError()



def shuffled(l: list) -> list:
    l_copy = l.copy()
    random.shuffle(l_copy)
    return l_copy

def avg(l: list) -> float | None:
    if len(l) == 0:
        return None
    else:
        return sum(l)/len(l)



def join_lines(lines: Iterable[str]) -> str:
    return '\n'.join(lines)
    # print(list(lines))
    # res: str = ""
    # for (i, line) in enumerate(lines):
    #     print(f"{i=}, {line=}")
    #     res += ('\n' if i != 0 else "") + line
    # return res

def count_start(string: str, character: char=' ') -> int:
    for (i, c) in enumerate(string):
        if c != character:
            return i
    else:
        return len(string)

def map_by_line(function: Callable[[str], str], string: str) -> str:
    return join_lines(map(function, string.splitlines()))

def trim_by_first_line(string: str) -> str:
    # print(string.splitlines())
    string = join_lines(string.splitlines()[1:-1])
    # print(string.splitlines())
    first_line_shift = count_start(string.splitlines()[0])
    return map_by_line(lambda line: line[first_line_shift:], string)



@dataclass
class JapaneseLetter:
    transliteration_to_latin: str
    hiragana: str
    katakana: str

ALL_LETTERS: list[JapaneseLetter] = [
    JapaneseLetter("a", "あ", "ア"),
    JapaneseLetter("i", "い", "イ"),
    JapaneseLetter("u", "う", "ウ"),
    JapaneseLetter("e", "え", "エ"),
    JapaneseLetter("o", "お", "オ"),
    JapaneseLetter("n", "ん", "ン"),

    JapaneseLetter("ka", "か", "カ"),
    JapaneseLetter("ki", "き", "キ"),
    JapaneseLetter("ku", "く", "ク"),
    JapaneseLetter("ke", "け", "ケ"),
    JapaneseLetter("ko", "こ", "コ"),

    JapaneseLetter("ga", "が", "ガ"),
    JapaneseLetter("gi", "ぎ", "ギ"),
    JapaneseLetter("gu", "ぐ", "グ"),
    JapaneseLetter("ge", "げ", "ゲ"),
    JapaneseLetter("go", "ご", "ゴ"),

    JapaneseLetter("sa", "さ", "サ"),
    JapaneseLetter("shi", "し", "シ"),
    JapaneseLetter("su", "す", "ス"),
    JapaneseLetter("se", "せ", "セ"),
    JapaneseLetter("so", "そ", "ソ"),

    JapaneseLetter("za", "ざ", "ザ"),
    JapaneseLetter("zhi", "じ", "ジ"),
    JapaneseLetter("zu", "ず", "ズ"),
    JapaneseLetter("ze", "ぜ", "ゼ"),
    JapaneseLetter("zo", "ぞ", "ゾ"),

    JapaneseLetter("ta", "た", "タ"),
    JapaneseLetter("chi", "ち", "チ"),
    JapaneseLetter("tsu", "つ", "ツ"),
    JapaneseLetter("te", "て", "テ"),
    JapaneseLetter("to", "と", "ト"),

    #TODO?: di, du -> ヂ ヅ 
    JapaneseLetter("da", "だ", "ダ"),
    JapaneseLetter("de", "で", "デ"),
    JapaneseLetter("do", "ど", "ド"),

    JapaneseLetter("na", "な", "ナ"),
    JapaneseLetter("ni", "に", "ニ"),
    JapaneseLetter("nu", "ぬ", "ヌ"),
    JapaneseLetter("ne", "ね", "ネ"),
    JapaneseLetter("no", "の", "ノ"),

    JapaneseLetter("ha", "は", "ハ"),
    JapaneseLetter("hi", "ひ", "ヒ"),
    JapaneseLetter("fu", "ふ", "フ"),
    JapaneseLetter("he", "へ", "ヘ"),
    JapaneseLetter("ho", "ほ", "ホ"),

    JapaneseLetter("ba", "ば", "バ"),
    JapaneseLetter("bi", "び", "ビ"),
    JapaneseLetter("bu", "ぶ", "ブ"),
    JapaneseLetter("be", "べ", "ベ"),
    JapaneseLetter("bo", "ぼ", "ボ"),

    JapaneseLetter("pa", "ぱ", "パ"),
    JapaneseLetter("pi", "ぴ", "ピ"),
    JapaneseLetter("pu", "ぷ", "プ"),
    JapaneseLetter("pe", "ぺ", "ペ"),
    JapaneseLetter("po", "ぽ", "ポ"),

    JapaneseLetter("ma", "ま", "マ"),
    JapaneseLetter("mi", "み", "ミ"),
    JapaneseLetter("mu", "む", "ム"),
    JapaneseLetter("me", "め", "メ"),
    JapaneseLetter("mo", "も", "モ"),

    JapaneseLetter("ra", "ら", "ラ"),
    JapaneseLetter("ri", "り", "リ"),
    JapaneseLetter("ru", "る", "ル"),
    JapaneseLetter("re", "れ", "レ"),
    JapaneseLetter("ro", "ろ", "ロ"),

    JapaneseLetter("ya", "や", "ヤ"),
    JapaneseLetter("yu", "ゆ", "ユ"),
    JapaneseLetter("yo", "よ", "ヨ"),

    #TODO?: wi -> ヰ,   we -> ヱ
    JapaneseLetter("wa", "わ", "ワ"),
    JapaneseLetter("O", "を", "ヲ"),
]



@dataclass
class JapaneseKanji:
    symbol: str
    transliteration_to_latin: str
    translation_to_english: str

ALL_KANJI: list[JapaneseKanji] = [
    JapaneseKanji("私", "watashi", "i"),
]

JapaneseSymbol: TypeAlias = JapaneseLetter | JapaneseKanji

ALL_SYMBOLS: list[JapaneseSymbol] = ALL_LETTERS + ALL_KANJI



# TestTypeType: TypeAlias = collections.namedtuple("TestType", ["n", "name"])
# class TestType:
#     Hiragana             = TestTypeType(1, "Hiragana")
#     Katakana             = TestTypeType(2, "Katakana")
#     AllLetters           = TestTypeType(3, "All Letters (Hiragana + Katakana)")
#     KanjiTranslation     = TestTypeType(4, "Kanji Translation")
#     KanjiTransliteration = TestTypeType(5, "Kanji Transliteration")
#     All                  = TestTypeType(6, "All (Kanji + Hiragana + Katakana)")

class TestType(Enum):
    # enhance your enum
    def get_size() -> int: return len(TestType._member_names_)
    def get_by_index(index: int) -> "TestType":
        assert(0 <= index < TestType.get_size())
        # return TestType(TestType._member_names_[index])
        return list(TestType)[index]
    Hiragana = "Hiragana"
    Katakana = "Katakana"
    KanaAll = "All Letters (Hiragana + Katakana)"
    KanjiTranslation = "Kanji Translation"
    KanjiTransliteration = "Kanji Transliteration"
    KanjiAll = "All Kanji (Translation + Transliteration)"
    All = "All (All Kana + All Kanji)"

@dataclass
class Test:
    question: str
    answer: str
    message: str

class TestLength(Enum):
    # enhance your enum
    def get_size() -> int: return len(TestLength._member_names_)
    def get_by_index(index: int) -> "TestLength":
        assert(0 <= index < TestLength.get_size())
        # return TestLength(TestLength._member_names_[index])
        return list(TestLength)[index]
    Endless = "Endless"
    OnceEverySymbol = "Once every symbol"
    NSymbols = "N symbol"



def ask_question_and_check_answer(test: Test) -> bool | None:
    answer = input('\n'+test.message+'\nAnswer: ')
    match answer:
        case test.answer:
            print("Correct.")
        case Constants.STOP_SEQ:
            return None
        case _:
            print(f"WRONG! Correct answer is: {test.answer}")
    return answer == test.answer


def ask_questions(tests: list[Test], test_len: TestLength, test_len_n: None | int) -> list[bool]:
    statistics = []

    def ask_question_and_check_answer_and_update_statistics(test: Test) -> bool:
        is_answer_correct = ask_question_and_check_answer(test)
        # TODO?
        #if is_answer_correct == None:
        #    return@ask_questions statistics
        if is_answer_correct != None:
            statistics.append(is_answer_correct)
        return is_answer_correct == None

    match test_len:
        case TestLength.Endless:
            assert(test_len_n == None)
            while True:
                for test in shuffled(tests):
                    is_exited = ask_question_and_check_answer_and_update_statistics(test)
                    if is_exited: return statistics
        case TestLength.OnceEverySymbol:
            assert(test_len_n == None)
            for test in shuffled(tests):
                is_exited = ask_question_and_check_answer_and_update_statistics(test)
                if is_exited: return statistics
        case TestLength.NSymbols:
            assert(test_len_n != None)
            # TODO: fix for `test_len_n` > `len(tests)`
            for test in shuffled(tests)[:test_len_n]:
                is_exited = ask_question_and_check_answer_and_update_statistics(test)
                if is_exited: return statistics
        case _:
            unreachable()
    return statistics


def generate_tests(test_type: TestType) -> list[Test]:
    tests: list[Test] = []

    def generate_tests_for_hiragana() -> list[Test]:
        return [
            Test(
                letter.hiragana,
                letter.transliteration_to_latin,
                f"What is transliteration for {letter.hiragana}?"
            )
            for letter in ALL_LETTERS
        ]

    def generate_tests_for_katakana() -> list[Test]:
        return [
            Test(
                letter.katakana,
                letter.transliteration_to_latin,
                f"What is transliteration for {letter.katakana}?"
            )
            for letter in ALL_LETTERS
        ]

    def generate_tests_for_kanji_translation() -> list[Test]:
        return [
            Test(
                kanji.symbol,
                kanji.translation_to_english,
                f"What is translation of {kanji.symbol}?"
            )
            for kanji in ALL_KANJI
        ]

    def generate_tests_for_kanji_transliteration() -> list[Test]:
        return [
            Test(
                kanji.symbol,
                kanji.transliteration_to_latin,
                f"What is transliteration of {kanji.symbol}?"
            )
            for kanji in ALL_KANJI
        ]

    match test_type:
        case TestType.Hiragana:
            tests += generate_tests_for_hiragana()
        case TestType.Katakana:
            tests += generate_tests_for_katakana()
        case TestType.KanaAll:
            tests += generate_tests_for_hiragana()
            tests += generate_tests_for_katakana()
        case TestType.KanjiTranslation:
            tests += generate_tests_for_kanji_translation()
        case TestType.KanjiTransliteration:
            tests += generate_tests_for_kanji_transliteration()
        case TestType.KanjiAll:
            tests += generate_tests_for_kanji_translation()
            tests += generate_tests_for_kanji_transliteration()
        case TestType.All:
            tests += generate_tests_for_hiragana()
            tests += generate_tests_for_katakana()
        case _:
            unreachable()

    return tests


def print_statistics(statistics: list[bool]):
    match avg(statistics):
        case float(fraction):
            percentage = 100.0 * fraction
            percentage_str = f"{percentage:.2f}%"
        case None:
            percentage_str = "--"
        case _:
            unreachable()
    print(f"\nCorrect percentage: {percentage_str}")


def ask_test_type() -> TestType:
    print("Available test types:")
    for (i, test_type) in enumerate(TestType):
        print(f"{i+1}) {test_type.value}")
    chosen_option: int = int(input(f"Choose test type (1-{len(TestType)}): ")) - 1
    test_type = TestType.get_by_index(chosen_option)
    return test_type


def ask_test_len() -> tuple[TestLength, None | int]:
    print("Available test lenghts:")
    for (i, test_type) in enumerate(TestLength):
        print(f"{i+1}) {test_type.value}")
    chosen_option: int = int(input(f"Choose test lenght (1-{len(TestLength)}): ")) - 1
    test_len = TestLength.get_by_index(chosen_option)
    if test_len == TestLength.NSymbols:
        n = int(input("How many times? "))
    else:
        n = None
    return (test_len, n)



def main() -> None:
    print(trim_by_first_line(f"""
        Learn Japanese program by dmyTRUEk (v{__version__})

        To exit input `{Constants.STOP_SEQ}`.
    """))
    print()
    test_type = ask_test_type()
    test_len, test_len_n = ask_test_len()

    tests = generate_tests(test_type)
    statistics = ask_questions(tests, test_len, test_len_n)

    print_statistics(statistics)





if __name__ == "__main__":
    main()
    print()

