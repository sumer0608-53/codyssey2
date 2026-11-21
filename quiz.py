from dataclasses import dataclass


@dataclass(frozen=True)
class Quiz:
    question: str
    choices: list[str]
    answer: int

    def __post_init__(self) -> None:
        if not isinstance(self.question, str) or not self.question.strip():
            raise ValueError("문제는 비어 있을 수 없습니다.")
        if not isinstance(self.choices, list) or len(self.choices) != 4:
            raise ValueError("선택지는 네 개여야 합니다.")
        if not all(isinstance(choice, str) and choice.strip() for choice in self.choices):
            raise ValueError("선택지는 비어 있을 수 없습니다.")
        if type(self.answer) is not int or not 1 <= self.answer <= 4:
            raise ValueError("정답 번호는 1~4여야 합니다.")

    def show(self, index: int) -> None:
        print(f"\n[{index}] {self.question}")
        for number, choice in enumerate(self.choices, 1):
            print(f"  {number}. {choice}")

    def is_correct(self, number: int) -> bool:
        return number == self.answer
