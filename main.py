# Learn Japanese program by dmyTRUEk

__version__ = "0.3.2"

from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from sys import exit as sys_exit

from colorama import Fore as fg
#from colorama import Back as bg
from colorama import Style

from enhance_enum import enhance_enum
from extensions import unreachable, shuffled, avg, trim_by_first_line
from kana import KANA
from kanji import KANJI



class Constants:
    COMMAND_STOP: str = ";;"
    EXITING: str = "\nExiting..."



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


def colorize(s: str, /, *, fg=None, bg=None) -> str:
    is_fg: bool = fg is not None
    is_bg: bool = bg is not None
    return (
        (fg if is_fg else "") +
        (bg if is_bg else "") +
        s +
        (Style.RESET_ALL if (is_fg or is_bg) else "")
    )


def ask_questions(tests: list[Test], test_len: TestLength) -> tuple[list[bool], list[Test]]:
    statistics: list[bool] = []
    mistakes: list[Test] = []

    def ask_check_update(test: Test) -> bool:
        # this function will:
        # 1. ask question
        # 2. check answer
        # 3. update statistics
        print()
        print(test.message_to_fmt.format(test.question))

        user_answer = input("Answer: ")
        if user_answer == Constants.COMMAND_STOP: return True

        is_answered_correctly = test.chech_answer(user_answer)

        if is_answered_correctly:
            print(colorize("Correct.", fg=fg.GREEN))
        else:
            print(colorize(f"WRONG! Correct answer: {test.answer}", fg=fg.RED))
            mistaken_test = deepcopy(test)
            mistaken_test.user_answer = user_answer
            if mistaken_test not in mistakes:
                mistakes.append(mistaken_test)

        statistics.append(is_answered_correctly)
        # TODO?
        # return@ask_questions statistics
        return False

    try:
        match test_len:
            case TestLength.Endless:
                while True:
                    for test in shuffled(tests):
                        is_exited = ask_check_update(test)
                        if is_exited: return (statistics, mistakes)
            case TestLength.OnceEverySymbol:
                for test in shuffled(tests):
                    is_exited = ask_check_update(test)
                    if is_exited: return (statistics, mistakes)
            case TestLength.CertainAmount:
                assert(hasattr(test_len, "n"))
                tests_shuffle: list[Test] = []
                for _ in range(test_len.n):
                    if len(tests_shuffle) == 0:
                        tests_shuffle = shuffled(tests)
                    test = tests_shuffle.pop()
                    is_exited = ask_check_update(test)
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
    if test_len == TestLength.CertainAmount:
        test_len.n = int(input("How many times? "))
    return test_len


def print_statistics(statistics: list[bool]):
    match avg(statistics):
        case float(fraction):
            percentage = 100.0 * fraction
            percentage_str = f"{percentage:.1f}%"
        case None:
            percentage_str = "--"
        case _:
            unreachable()
    print(f"Percentage of correct answers: {percentage_str}")


def print_mistakes(mistakes: list[Test]):
    print(f"Total mistakes: " + colorize(str(len(mistakes)), fg=fg.RED) + ". Your mistakes:")
    for (i, test) in enumerate(mistakes):
        assert(test.user_answer is not None)
        print(f"{i+1}. {test.message_to_fmt.format(test.question)}")
        print("   Correct answer: " + colorize(str(test.answer), fg=fg.GREEN))
        print("   Your    answer: " + colorize(test.user_answer, fg=fg.RED))


def main() -> None:
    print(trim_by_first_line(f"""
        Learn Japanese by dmyTRUEk, v{__version__}

        To exit input `{Constants.COMMAND_STOP}` or press Ctrl+C.
    """))
    print()

    test_type = ask_test_type()
    print()
    test_len = ask_test_len()

    tests = generate_tests(test_type)
    statistics, mistakes = ask_questions(tests, test_len)

    print()
    input("Press Enter to see results.")
    if mistakes:
        print()
        print_mistakes(mistakes)
    print()
    print_statistics(statistics)

    print()





if __name__ == "__main__":
    main()

