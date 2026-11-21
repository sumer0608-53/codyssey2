import json
from dataclasses import asdict
from pathlib import Path
from tempfile import NamedTemporaryFile

from questions import default_quizzes
from quiz import Quiz


def load_state(path: Path) -> tuple[list[Quiz], int | None]:
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(state, dict) or not isinstance(state.get("quizzes"), list):
            raise ValueError("퀴즈 목록을 읽을 수 없습니다.")
        score = state["best_score"]
        if score is not None and (type(score) is not int or not 0 <= score <= 100):
            raise ValueError("최고 점수는 0~100점이어야 합니다.")
        quizzes = [Quiz(**item) for item in state["quizzes"]]
    except FileNotFoundError:
        return default_quizzes(), None
    except (OSError, ValueError, TypeError, KeyError):
        print("저장 파일을 읽을 수 없어 기본 퀴즈로 시작합니다.")
        return default_quizzes(), None
    print(f"저장 데이터를 불러왔습니다. (퀴즈 {len(quizzes)}개)")
    return quizzes, score


def save_state(path: Path, quizzes: list[Quiz], best_score: int | None) -> bool:
    state = {"quizzes": [asdict(quiz) for quiz in quizzes], "best_score": best_score}
    temporary = None
    try:
        with NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, prefix=".state-",
            suffix=".tmp", delete=False,
        ) as file:
            temporary = Path(file.name)
            json.dump(state, file, ensure_ascii=False, indent=2)
            file.write("\n")
        temporary.replace(path)
    except OSError:
        print("저장에 실패했습니다. 폴더의 쓰기 권한을 확인하세요.")
        return False
    finally:
        if temporary is not None:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass
    return True
