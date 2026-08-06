from quiz_game import QuizGame


def main():

    game = QuizGame()

    game.load_state()

    while True:
        try:
            menu = game.show_menu()

            if menu == 1:
                game.start_quiz()
                pass

            elif menu == 2:
                game.show_quiz_list()

            elif menu == 3:
                game.show_score()

            elif menu == 0:
                game.save_state()
                print("프로그램 종료합니다")
                break

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: 안전하게 종료합니다.")
            game.save_state()
            break

        except EOFError:
            print("\nEOFError: 안전하게 종료합니다.")
            game.save_state()
            break

        except Exception as e:
            print(f"오류 발생: {e}")
            game.save_state()
            break
            


if __name__ == "__main__":
    main()