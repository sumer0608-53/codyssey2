def ask_number(prompt: str, low: int, high: int) -> int:
    while True:
        raw = input(prompt).strip()
        if not raw:
            print("빈 입력입니다. 번호를 입력하세요.")
            continue
        try:
            number = int(raw)
        except ValueError:
            print("숫자를 입력하세요.")
            continue
        if low <= number <= high:
            return number
        print(f"{low}~{high} 사이의 번호를 입력하세요.")


def ask_text(prompt: str) -> str:
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("빈 입력입니다. 내용을 입력하세요.")
