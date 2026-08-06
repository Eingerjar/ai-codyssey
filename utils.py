def get_int_input(prompt, min_value, max_value):
    while True:
        try:
            value = input(prompt).strip()

            if not value:
                print("입력값을 입력해주세요.")
                continue

            value = int(value)

            if value < min_value or value > max_value:
                print(f"{min_value}부터 {max_value}까지 입력해주세요.")
                continue

            return value

        except ValueError:
            print("숫자를 입력해주세요.")