from utils import get_int_input
from default_quizzes import get_default_quizzes


MENU = f"""========================================
    🎯 나만의 퀴즈 게임 🎯
========================================
    1. 퀴즈 풀기
    2. 퀴즈 추가
    3. 퀴즈 목록
    4. 점수 확인
    0. 종료
========================================"""

class QuizGame:
    def __init__(self):
        self.quiz_list = get_default_quizzes()
        self.score = 0

    def load_state(self):
        # Load the game state from a file or database
        pass

    def save_state(self):
        # Save the game state to a file or database
        pass

    def show_menu(self):
        print(MENU)
        return get_int_input("메뉴를 선택하세요: ", 0, 4)

    def start_quiz(self):
        # Start the quiz
        pass

    def show_quiz_list(self):
        # Show the list of quizzes
        pass

    def show_score(self):
        # Show the current score
        pass