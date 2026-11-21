from pathlib import Path

from prompts import ask_number, ask_text
from questions import default_quizzes
from quiz import Quiz
from storage import load_state, save_state


MENU = """
=== 파이썬 한 문제 ===
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료"""


class QuizGame:
    def __init__(self, state_path: Path) -> None:
        self.state_path = state_path
        self.quizzes, self.best_score = self.load()
        self.dirty = False

    def load(self) -> tuple[list[Quiz], int | None]:
        return load_state(self.state_path)

    def save(self) -> bool:
        if save_state(self.state_path, self.quizzes, self.best_score):
            self.dirty = False
            return True
        return False

    def run(self) -> None:
        actions = {
            1: self.play,
            2: self.add_quiz,
            3: self.list_quizzes,
            4: self.show_score,
        }
        try:
            while True:
                print(MENU)
                selection = ask_number("선택 (1~5): ", 1, 5)
                if selection == 5:
                    break
                actions[selection]()
        except (KeyboardInterrupt, EOFError):
            print("\n입력이 중단되어 게임을 종료합니다.")
        finally:
            if self.dirty:
                self.save()
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
        if self.best_score is None or score > self.best_score:
            self.best_score = score
            self.dirty = True
            self.save()
            print("새로운 최고 점수입니다!")

    def add_quiz(self) -> None:
        print("\n새 퀴즈 등록")
        question = ask_text("문제: ")
        choices = [ask_text(f"선택지 {number}: ") for number in range(1, 5)]
        answer = ask_number("정답 번호 (1~4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.dirty = True
        if self.save():
            print("퀴즈가 추가되었습니다.")
        else:
            print("퀴즈를 추가했지만 파일에 저장하지 못했습니다.")

    def list_quizzes(self) -> None:
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return
        print(f"등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        for index, quiz in enumerate(self.quizzes, 1):
            print(f"[{index}] {quiz.question}")

    def show_score(self) -> None:
        if self.best_score is None:
            print("아직 퀴즈를 풀지 않았습니다.")
            return
        print(f"최고 점수: {self.best_score}점")
