# Learn Japanese program by dmyTRUEk

__version__ = "0.2.1"

from sys import exit as sys_exit

from dataclasses import dataclass
from enum import Enum
from typing import Callable, Iterable, TypeAlias

import random

from colorama import Fore as fg
from colorama import Back as bg
from colorama import Style

import copy



char: TypeAlias = str

class Constants:
    COMMAND_STOP: str = "exit;"
    EXITING: str = "\nExiting..."



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

def count_start(string: str, character: char=' ') -> int:
    for (i, c) in enumerate(string):
        if c != character:
            return i
    else:
        return len(string)

def map_by_line(function: Callable[[str], str], string: str) -> str:
    return join_lines(map(function, string.splitlines()))

def trim_by_first_line(string: str) -> str:
    string = join_lines(string.splitlines()[1:-1])
    first_line_shift = count_start(string.splitlines()[0])
    return map_by_line(lambda line: line[first_line_shift:], string)



def print_colored(*args, **kwargs):
    BG: str = "bg"
    FG: str = "fg"
    if BG in kwargs:
        print(kwargs[BG], end="")
        del(kwargs[BG])
    if FG in kwargs:
        print(kwargs[FG], end="")
        del(kwargs[FG])
    print(*args, **kwargs)
    print(Style.RESET_ALL, end="")


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
    # TODO: impl multuple answers
    transliteration_to_latin: str | list[str]
    translation_to_english: str | list[str]

ALL_KANJI: list[JapaneseKanji] = [
    #JapaneseKanji("", "", ""),

    # TODO: answer by numbers: 1-10
    JapaneseKanji("一", "ichi", ["1", "one"]),
    JapaneseKanji("二", "ni", ["2", "two"]),
    JapaneseKanji("三", "san", ["3", "three"]),
    JapaneseKanji("四", ["yon", "shi"], ["4", "four"]),
    JapaneseKanji("五", "go", ["5", "five"]),
    JapaneseKanji("六", "roku", ["6", "six"]),
    JapaneseKanji("七", ["shichi", "nana"], ["7", "seven"]),
    JapaneseKanji("八", "hachi", ["8", "eight"]),
    JapaneseKanji("九", "kyu", ["9", "nine"]),
    JapaneseKanji("十", "ju", ["10", "ten"]),
    JapaneseKanji("百", "hyaku", ["100", "hundred"]),
    JapaneseKanji("千", "sen", ["1000", "thousand", "1_000"]),
    JapaneseKanji("万", "man", ["10000", "ten thousand", "10_000"]),

    JapaneseKanji("私", "watashi", "i"),
]



JapaneseSymbol: TypeAlias = JapaneseLetter | JapaneseKanji

ALL_SYMBOLS: list[JapaneseSymbol] = ALL_LETTERS + ALL_KANJI



def enhance_enum(cls):
    assert(cls is not None)
    def get_by_index(index: int):
        assert(isinstance(index, int))
        assert(0 <= index < len(cls))
        return list(cls)[index]
    setattr(cls, "get_by_index", get_by_index)
    return cls



@enhance_enum
class TestType(Enum):
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
    answer: str | list[str]
    message_to_fmt: str
    user_answer: None | str = None

@enhance_enum
class TestLength(Enum):
    OnceEverySymbol = "Once every symbol"
    NSymbols = "N symbol"
    Endless = "Endless"



def ask_questions(tests: list[Test], test_len: TestLength) -> tuple[list[bool], list[Test]]:
    statistics: list[bool] = []
    mistakes: list[Test] = []

    def ask_question_and_check_answer_and_update_statistics(test: Test) -> bool:
        print()
        print(test.message_to_fmt.format(test.question))

        user_answer = input("Answer: ")
        if user_answer == Constants.COMMAND_STOP: return True

        match test.answer:
            case str(correct_answer):
                is_answered_correctly = (user_answer == correct_answer)
            case list(correct_answers):
                is_answered_correctly = (user_answer in correct_answers)
            case _:
                unreachable()

        if is_answered_correctly:
            print_colored("Correct.", fg=fg.GREEN)
        else:
            print_colored(f"WRONG! Correct answer is: {test.answer}", fg=fg.RED)
            mistaken_test = copy.deepcopy(test)
            mistaken_test.user_answer = user_answer
            if mistaken_test not in mistakes:
                mistakes.append(mistaken_test)

        statistics.append(user_answer == test.answer)
        # TODO?
        # return@ask_questions statistics
        return False

    try:
        match test_len:
            case TestLength.Endless:
                while True:
                    for test in shuffled(tests):
                        is_exited = ask_question_and_check_answer_and_update_statistics(test)
                        if is_exited: return (statistics, mistakes)
            case TestLength.OnceEverySymbol:
                for test in shuffled(tests):
                    is_exited = ask_question_and_check_answer_and_update_statistics(test)
                    if is_exited: return (statistics, mistakes)
            case TestLength.NSymbols:
                assert(hasattr(test_len, "n"))
                tests_shuffle: list[Test] = []
                for _ in range(test_len.n):
                    if len(tests_shuffle) == 0:
                        tests_shuffle = shuffled(tests)
                    test = tests_shuffle.pop()
                    is_exited = ask_question_and_check_answer_and_update_statistics(test)
                    if is_exited: return (statistics, mistakes)
            case _:
                unreachable()
    except KeyboardInterrupt:
        print(Constants.EXITING)
    return (statistics, mistakes)


def generate_tests(test_type: TestType) -> list[Test]:
    tests: list[Test] = []

    def generate_tests_for_hiragana() -> list[Test]:
        return [
            Test(
                letter.hiragana,
                letter.transliteration_to_latin,
                "What is transliteration for {}?"
            )
            for letter in ALL_LETTERS
        ]

    def generate_tests_for_katakana() -> list[Test]:
        return [
            Test(
                letter.katakana,
                letter.transliteration_to_latin,
                "What is transliteration for {}?"
            )
            for letter in ALL_LETTERS
        ]

    def generate_tests_for_kanji_translation() -> list[Test]:
        return [
            Test(
                kanji.symbol,
                kanji.translation_to_english,
                "What is translation of {}?"
            )
            for kanji in ALL_KANJI
        ]

    def generate_tests_for_kanji_transliteration() -> list[Test]:
        return [
            Test(
                kanji.symbol,
                kanji.transliteration_to_latin,
                "What is transliteration of {}?"
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


def ask_test_type() -> TestType:
    print("Available test types:")
    for (i, test_type) in enumerate(TestType):
        print(f"{i+1}) {test_type.value}")
    try:
        chosen_option: int = int(input(f"Choose test type (1-{len(TestType)}): ")) - 1
    except KeyboardInterrupt:
        print(Constants.EXITING)
        sys_exit(0)
    test_type = TestType.get_by_index(chosen_option)
    return test_type


def ask_test_len() -> TestLength:
    print("Available test lenghts:")
    for (i, test_type) in enumerate(TestLength):
        print(f"{i+1}) {test_type.value}")
    try:
        chosen_option: int = int(input(f"Choose test lenght (1-{len(TestLength)}): ")) - 1
    except KeyboardInterrupt:
        print(Constants.EXITING)
        sys_exit(0)
    test_len = TestLength.get_by_index(chosen_option)
    if test_len == TestLength.NSymbols:
        test_len.n = int(input("How many times? "))
    return test_len


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


def print_mistakes(mistakes: list[Test]):
    print(f"\nTotal mistakes: ", end="")
    print_colored(len(mistakes), end="", fg=fg.RED)
    print(". Your mistakes:")
    for (i, test) in enumerate(mistakes):
        print(f"{i+1}. {test.message_to_fmt.format(test.question)}")
        print("   Correct answer: ", end="")
        print_colored(test.answer, fg=fg.GREEN)
        print("   Your    answer: ", end="")
        print_colored(test.user_answer, fg=fg.RED)


def main() -> None:
    print(trim_by_first_line(f"""
        Learn Japanese program by dmyTRUEk (v{__version__})

        To exit input `{Constants.COMMAND_STOP}` or press Ctrl+C.
    """))
    print()

    test_type = ask_test_type()
    test_len = ask_test_len()

    tests = generate_tests(test_type)
    statistics, mistakes = ask_questions(tests, test_len)

    if mistakes:
        print_mistakes(mistakes)
    print_statistics(statistics)

    print()





if __name__ == "__main__":
    main()

