from utils import get_int_input
from default_quizzes import get_default_quizzes
import json
from quiz import Quiz

MENU = f"""========================================
    🎯 나만의 퀴즈 게임 🎯
========================================
    1. 퀴즈 풀기
    2. 퀴즈 추가
    3. 퀴즈 목록
    4. 점수 확인
    0. 종료
========================================"""

STATE_FILE = "state.json"

class QuizGame:
    def __init__(self):
        self.quiz_list = []
        self.best_score = -1

    def add_quiz(self):
        pass

    def load_state(self):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quiz_list = [Quiz.from_dict(quiz_data) for quiz_data in data["quizzes"]]
                self.best_score = data["best_score"]
            print("저장된 상태를 불러왔습니다.")
        except FileNotFoundError:
            print("저장된 상태가 없습니다. 기본 퀴즈를 불러옵니다.")
            self.quiz_list = get_default_quizzes()
            self.save_state()
        except json.JSONDecodeError:
            print("저장된 상태를 불러오는 중 오류가 발생했습니다. 기본 퀴즈를 불러옵니다.")
            self.quiz_list = get_default_quizzes()
            self.save_state()
        except Exception as e:
            print(f"상태를 불러오는 중 오류가 발생했습니다 {type(e).__name__}: {e}. 기본 퀴즈를 불러옵니다.")
            self.quiz_list = get_default_quizzes()
            self.save_state()

    def save_state(self):
        data = {
            "quizzes": [quiz.to_dict() for quiz in self.quiz_list],
            "best_score": self.best_score
        }
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"상태를 저장하는 중 오류가 발생했습니다 {type(e).__name__}: {e}.")

    def show_menu(self):
        print(MENU)
        return get_int_input("메뉴를 선택하세요: ", 0, 4)

    def start_quiz(self):
        correct_answers = 0
        if not self.quiz_list:
            print("퀴즈가 없습니다. 퀴즈를 추가해주세요.")
            return
        for quiz in self.quiz_list:
            print("\n----------------------------------------")
            quiz.display()
            user_answer = get_int_input("정답을 선택하세요: ", 1, 4)

            if quiz.check_answer(user_answer):
                print("\n✅ 정답입니다!\n")
                correct_answers += 1
            else:
                print(f"\n❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")
        score = int(correct_answers / len(self.quiz_list) * 100)
        if score > self.best_score:
            self.best_score = score
            self.save_state()
        print(f"\n⭐️퀴즈 종료! 당신의 점수는 {score}점입니다.⭐️\n")

    def show_quiz_list(self):
        if not self.quiz_list:
            print("퀴즈가 없습니다. 퀴즈를 추가해주세요.")
            return
        print("\n퀴즈 목록:")
        for index, quiz in enumerate(self.quiz_list, start=1):
            print(f"{index}. {quiz.question}")
        pass

    def show_score(self):
        if self.best_score == -1:
            print("\n아직 퀴즈를 풀지 않았습니다. 퀴즈를 풀어보세요!\n")
        else:
            print(f"\n🏆 최고 점수: {self.best_score}점 🏆\n")