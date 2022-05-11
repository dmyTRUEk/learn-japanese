"""
Learn Japanese program by dmyTRUEk
"""

__version__ = "0.4.0"

from copy import deepcopy
from sys import exit as sys_exit

from colorama import Style
from colorama import Fore as fg
#from colorama import Back as bg

from extensions_python import unreachable, avg, trim_by_first_line
from test_class import Test
from test_length_enum import TestLength
from test_type_enum import TestType
from tests_generation import generate_tests_certain_amount, generate_tests_endless, generate_tests_once



class Constants:
    COMMAND_STOP : str = ";;"
    EXITING      : str = "\nExiting..."
    PROMPT_ANSWER: str = "Answer: "
    CORRECT      : str = "Correct."
    WRONG_TO_FMT : str = "WRONG! Correct answer: {}"



def colorize(s: str, /, *, fg=None, bg=None) -> str:
    is_fg: bool = fg is not None
    is_bg: bool = bg is not None
    return (
        (fg if is_fg else "") +
        (bg if is_bg else "") +
        s +
        (Style.RESET_ALL if (is_fg or is_bg) else "")
    )


def run_test(test_type: TestType, test_len: TestLength) -> tuple[list[bool], list[Test]]:
    statistics: list[bool] = []
    mistakes: list[Test] = []

    def ask_check_update(test: Test) -> bool:
        # this function will:
        # 1. ask question
        # 2. check answer
        # 3. update statistics
        print()
        print(test.get_message())

        user_answer = input(Constants.PROMPT_ANSWER)
        if user_answer == Constants.COMMAND_STOP: return True

        is_answered_correctly = test.chech_answer(user_answer)
        statistics.append(is_answered_correctly)

        if is_answered_correctly:
            print(colorize(Constants.CORRECT, fg=fg.GREEN))
        else:
            print(colorize(Constants.WRONG_TO_FMT.format(test.answer), fg=fg.RED))
            mistaken_test = deepcopy(test)
            mistaken_test.user_answer = user_answer
            if mistaken_test not in mistakes:
                mistakes.append(mistaken_test)

        # TODO?
        # return@ask_questions statistics
        return False

    try:
        match test_len:
            case TestLength.OnceEverySymbol:
                for test in generate_tests_once(test_type):
                    is_exited = ask_check_update(test)
                    if is_exited: break
            case TestLength.CertainAmount:
                assert(hasattr(test_len, "n"))
                for test in generate_tests_certain_amount(test_type, test_len.n):
                    is_exited = ask_check_update(test)
                    if is_exited: break
            case TestLength.Endless:
                for test in generate_tests_endless(test_type):
                    is_exited = ask_check_update(test)
                    if is_exited: break
            case _:
                unreachable()
    except KeyboardInterrupt:
        print(Constants.EXITING)
    return (statistics, mistakes)


def exit(additional_message: None | str = None):
    if additional_message is not None:
        print(additional_message)
    print(Constants.EXITING)
    sys_exit(0)


def ask_test_type() -> TestType:
    print("Available test types:")

    for (i, test_type) in enumerate(TestType):
        print(f"{i+1}) {test_type.value}")

    try:
        chosen_option: int = int(input(f"Choose test type (1-{len(TestType)}): ")) - 1
    except ValueError:
        exit("Not an integer number")
    except KeyboardInterrupt:
        exit()
    if chosen_option not in range(len(TestType)): exit("Number not in range.")

    test_type = list(TestType)[chosen_option]

    if test_type == TestType.KanaRandomWords:
        try:
            difficulty: int = int(input("Choose difficulty (average word len): "))
        except ValueError:
            exit("Not a floating point number")
        except KeyboardInterrupt:
            exit()
        test_type.difficulty = difficulty

    return test_type


def ask_test_len(test_type: TestType) -> TestLength:
    print("Available test lenghts:")

    test_lens: list[TestLength] = list(TestLength)
    if test_type == TestType.KanaRandomWords:
        test_lens.remove(TestLength.OnceEverySymbol)

    for (i, test_len) in enumerate(test_lens):
        print(f"{i+1}) {test_len.value}")

    try:
        chosen_option: int = int(input(f"Choose test lenght (1-{len(test_lens)}): ")) - 1
    except ValueError:
        exit("Not a number")
    except KeyboardInterrupt:
        exit()
    if chosen_option not in range(len(test_lens)): exit("Number not in range.")

    test_len = test_lens[chosen_option]
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
        print(f"{i+1}. {test.get_message()}")
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
    test_len = ask_test_len(test_type)

    statistics, mistakes = run_test(test_type, test_len)

    print()
    try:
        input("Press Enter or Ctrl+C to see results.")
    except KeyboardInterrupt:
        pass

    if mistakes:
        print()
        print_mistakes(mistakes)
    print()
    print_statistics(statistics)

    print()





if __name__ == "__main__":
    main()

