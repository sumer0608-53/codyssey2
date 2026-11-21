from quiz import Quiz


def default_quizzes() -> list[Quiz]:
    return [
        Quiz("Python에서 True와 False의 자료형은?", ["str", "int", "bool", "list"], 3),
        Quiz("목록의 끝에 항목을 하나 추가하는 메서드는?", ["append", "strip", "split", "keys"], 1),
        Quiz("키와 값의 쌍을 저장하는 자료형은?", ["list", "bool", "str", "dict"], 4),
        Quiz("len('Python')의 결과는?", ["5", "6", "7", "오류"], 2),
        Quiz("range(3)을 순회하면 어떤 숫자가 나오는가?", ["1, 2, 3", "0, 1, 2, 3", "0, 1, 2", "3"], 3),
        Quiz("발생한 예외를 처리하는 절을 시작하는 키워드는?", ["class", "except", "return", "else"], 2),
    ]
