"""
Learn Japanese program by dmyTRUEk
"""

__version__ = "0.6.0"

from copy import deepcopy
from sys import exit as sys_exit

from extensions_colorama import colorize, GREEN, RED
from extensions_pipe import all_, map_, uniq_
from extensions_python import find_first, unreachable, avg, trim_by_first_line
from test_class import Test
from test_length_enum import TestLength
from test_type_enum import TestType
from tests_generation import generate_tests_certain_amount, generate_tests_endless, generate_tests_once

# from kanji import JAPANESE_WORDS



class Constants:
    COMMAND_STOP : str = ";;"
    EXITING      : str = "\nExiting..."
    PROMPT_ANSWER: str = "Answer: "
    CORRECT      : str = "Correct."
    WRONG_TO_FMT : str = "WRONG! Correct answer: {}"




def run_test(test_types: list[TestType], test_len: TestLength) -> tuple[list[bool], list[Test]]:
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
            print(colorize(Constants.CORRECT, fg=GREEN))
        else:
            print(colorize(Constants.WRONG_TO_FMT.format(test.answer), fg=RED))
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
                for test in generate_tests_once(test_types):
                    is_exited = ask_check_update(test)
                    if is_exited: break
            case TestLength.CertainAmount:
                assert(hasattr(test_len, "n"))
                for test in generate_tests_certain_amount(test_types, test_len.n):
                    is_exited = ask_check_update(test)
                    if is_exited: break
            case TestLength.Endless:
                for test in generate_tests_endless(test_types):
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


def ask_test_types() -> list[TestType]:
    print("Available test types:")

    for (i, test_type) in enumerate(TestType):
        print(f"{i+1}) {test_type.value}")
    print("*) All")

    try:
        chosen_options_str: str = input(f"Choose test types: ")
        if chosen_options_str == "*":
            chosen_options: list[int] = [i+1 for i in range(len(TestType))]
        else:
            chosen_options: list[int] = chosen_options_str.replace(" ", "").split(",") | map_(lambda o: int(o))
    except ValueError:
        exit("Not an integers.")
    except KeyboardInterrupt:
        exit()

    if not chosen_options | all_(lambda o: 1 <= o <= len(TestType)):
        exit("Numbers not in valid range.")

    if len(chosen_options) != len(chosen_options | uniq_):
        exit("Duplication found.")

    test_types: list[TestType] = chosen_options | map_(lambda o: list(TestType)[o-1])

    if (found:=find_first(test_types, lambda t: t == TestType.KanaRandomWords)) is not None:
        try:
            difficulty: int = int(input("Choose difficulty (average word len): "))
        except ValueError:
            exit("Not a floating point number")
        except KeyboardInterrupt:
            exit()
        found.difficulty = difficulty

    return test_types


def ask_test_len(test_types: list[TestType]) -> TestLength:
    print("Available test lenghts:")

    test_lens: list[TestLength] = list(TestLength)
    if TestType.KanaRandomWords in test_types:
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
    print(f"Total mistakes: " + colorize(str(len(mistakes)), fg=RED) + ". Your mistakes:")
    for (i, test) in enumerate(mistakes):
        assert(test.user_answer is not None)
        print(f"{i+1}. {test.get_message()}")
        print("   Correct answer: " + colorize(str(test.answer), fg=GREEN))
        print("   Your    answer: " + colorize(test.user_answer, fg=RED))
        print()


def main() -> None:
    print(trim_by_first_line(f"""
        Learn Japanese by dmyTRUEk, v{__version__}

        To exit input `{Constants.COMMAND_STOP}` or press Ctrl+C.
    """))
    print()

    # for jw in JAPANESE_WORDS:
    #     print(jw)

    test_types: list[TestType] = ask_test_types()
    print()
    test_len: TestLength = ask_test_len(test_types)

    statistics, mistakes = run_test(test_types, test_len)

    print()
    try:
        input("Press Enter or Ctrl+C to see results.")
    except KeyboardInterrupt:
        pass

    print()
    if mistakes:
        print_mistakes(mistakes)
    print_statistics(statistics)

    print()





if __name__ == "__main__":
    main()

