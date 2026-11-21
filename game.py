from prompts import ask_number
from questions import default_quizzes


MENU = """
=== 파이썬 한 문제 ===
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료"""


class QuizGame:
    def __init__(self) -> None:
        self.quizzes = default_quizzes()

    def run(self) -> None:
        actions = {
            1: self.play,
        }
        try:
            while True:
                print(MENU)
                selection = ask_number("선택 (1~5): ", 1, 5)
                if selection == 5:
                    break
                action = actions.get(selection)
                if action is None:
                    print("준비 중입니다.")
                    continue
                action()
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 게임을 종료합니다.")
        print("게임을 종료합니다.")

    def play(self) -> None:
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        correct = 0
        total = len(self.quizzes)
        for index, quiz in enumerate(self.quizzes, 1):
            quiz.show(index)
            number = ask_number("정답 번호 (1~4): ", 1, 4)
            if quiz.is_correct(number):
                correct += 1
                print("정답입니다!")
            else:
                print(f"오답입니다. 정답: {quiz.answer}. {quiz.choices[quiz.answer - 1]}")
        score = correct * 100 // total
        print(f"결과: {total}문제 중 {correct}문제 정답 ({score}점)")
