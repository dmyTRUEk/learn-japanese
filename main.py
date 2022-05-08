# Learn Japanese program by dmyTRUEk

__version__ = "0.3.1"

from copy import deepcopy
from dataclasses import dataclass
from enum import Enum
from sys import exit as sys_exit

from colorama import Fore as fg
#from colorama import Back as bg
from colorama import Style

from enhance_enum import enhance_enum
from extensions import unreachable, shuffled, avg, trim_by_first_line
from kana import ALL_LETTERS
from kanji import ALL_KANJI



class Constants:
    COMMAND_STOP: str = "exit;"
    EXITING: str = "\nExiting..."




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
    NSymbols = "N symbols"
    Endless = "Endless"



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
            match test.answer:
                case str(correct_answer):
                    print_colored(f"WRONG! Correct answer is: {correct_answer}", fg=fg.RED)
                case list(correct_answers):
                    print_colored(f"WRONG! Correct answers are: {correct_answers}", fg=fg.RED)
                case _:
                    unreachable()
            mistaken_test = deepcopy(test)
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

