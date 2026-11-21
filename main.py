from pathlib import Path

from game import QuizGame


if __name__ == "__main__":
    QuizGame(Path(__file__).resolve().with_name("state.json")).run()
