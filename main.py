from prompts import ask_number


MENU = """
=== 파이썬 한 문제 ===
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록
4. 점수 확인
5. 종료"""


def main() -> None:
    try:
        while True:
            print(MENU)
            if ask_number("선택 (1~5): ", 1, 5) == 5:
                break
            print("준비 중입니다.")
    except (KeyboardInterrupt, EOFError):
        print("\n입력이 중단되어 게임을 종료합니다.")
    print("게임을 종료합니다.")


if __name__ == "__main__":
    main()
