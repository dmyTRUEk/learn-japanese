"""
Test class
"""

from extensions_python import unreachable



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

