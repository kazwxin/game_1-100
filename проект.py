import random
import sys


def clear_input_buffer():
    try:
        sys.stdin.flush()
    except (OSError, AttributeError):
        pass


def safe_int_input(prompt: str, min_val: int = None, max_val: int = None) -> int:
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Ошибка: ввод не может быть пустым. Попробуйте снова.")
            continue

        try:
            value = int(user_input)
        except ValueError:
            print("Ошибка: необходимо ввести целое число. Попробуйте снова.")
            continue

        if min_val is not None and value < min_val:
            print(f"Ошибка: число должно быть не меньше {min_val}. Попробуйте снова.")
            continue

        if max_val is not None and value > max_val:
            print(f"Ошибка: число должно быть не больше {max_val}. Попробуйте снова.")
            continue

        return value


def guess_with_hint(prompt: str, min_val: int, max_val: int, allow_zero: bool = False) -> int:
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("Ошибка: ввод не может быть пустым. Попробуйте снова.")
            continue

        try:
            value = int(user_input)
        except ValueError:
            print("Ошибка: необходимо ввести целое число. Попробуйте снова.")
            continue

        if allow_zero and value == 0:
            return 0

        if value < min_val or value > max_val:
            print(f"Ошибка: число должно быть от {min_val} до {max_val}. Попробуйте снова.")
            continue

        return value


def computer_guesses() -> None:
    print("\n--- Компьютер отгадывает ваше число ---")
    print("Задумайте число от 1 до 100. Нажмите Enter, когда будете готовы.")
    input()

    low, high = 1, 100
    attempts = 0

    print("Договоримся: я буду называть число, а вы отвечайте:")
    print("  • 1 - если я угадал")
    print("  • 2 - если задуманное число БОЛЬШЕ моего предположения")
    print("  • 3 - если задуманное число МЕНЬШЕ моего предположения")
    print("\nНачинаем!\n")

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print(f"Попытка {attempts}: Моё предположение → {guess}")

        feedback = safe_int_input("Ваш ответ (1=угадал, 2=больше, 3=меньше): ", 1, 3)

        if feedback == 1:
            print(f"\nУра! Я угадал число {guess} за {attempts} попыток!")
            return
        elif feedback == 2:
            low = guess + 1
            print("✅ Понял: ваше число БОЛЬШЕ. Продолжаю поиск...\n")
        else:  # feedback == 3
            high = guess - 1
            print("✅ Понял: ваше число МЕНЬШЕ. Продолжаю поиск...\n")

        if low > high:
            print("\nСтранно... Диапазон поиска пуст.")
            print("Возможно, вы ошиблись в ответах? Давайте начнём заново.")
            return


def player_guesses() -> None:
    print("\n--- Вы отгадываете число, загаданное компьютером ---")
    secret = random.randint(1, 100)
    attempts = 0

    print(f"Компьютер загадал число от 1 до 100.")
    print("Попробуйте угадать! После каждой попытки я буду подсказывать:")
    print("«Больше» — если ваше число МЕНЬШЕ загаданного")
    print("«Меньше» — если ваше число БОЛЬШЕ загаданного")
    print("(или введите 0, чтобы сдаться и узнать число)\n")

    while True:
        attempts += 1

        guess = guess_with_hint(f"Попытка {attempts}. Ваше число: ", 1, 100, allow_zero=True)

        if guess == 0:
            print(f"\nЖаль, что вы сдались! Компьютер загадал число {secret}.")
            if attempts > 1:
                print(f"Вы сделали {attempts - 1} попыт(ок/ки) до того, как сдаться.")
            else:
                print("Вы сдались, не сделав ни одной попытки!")
            return

        if guess < secret:
            print(f"БОЛЬШЕ! (ваше число {guess} меньше загаданного, нужно увеличить)\n")
        elif guess > secret:
            print(f"МЕНЬШЕ! (ваше число {guess} больше загаданного, нужно уменьшить)\n")
        else:
            print(f"\nПОЗДРАВЛЯЮ! Вы угадали число {secret} за {attempts} попыток!")

            if attempts == 1:
                print("Невероятно! Вы угадали с первой попытки!")
            elif attempts <= 5:
                print("Отличный результат!")
            elif attempts <= 10:
                print("Хорошая работа!")
            else:
                print("Главное - не сдаваться! В следующий раз получится быстрее!")
            return


def main() -> None:
    print("=" * 55)
    print("        Добро пожаловать в игру «Угадай число»!")
    print("=" * 55)

    while True:
        print("\nВыберите режим игры:")
        print("1. Компьютер загадывает, вы отгадываете")
        print("2. Вы загадываете, компьютер отгадывает (бинарный поиск)")
        print("3. Выход из игры")

        choice = safe_int_input("\nВаш выбор: ", 1, 3)

        if choice == 1:
            player_guesses()
        elif choice == 2:
            computer_guesses()
        else:  # choice == 3
            print("\nСпасибо за игру! До свидания!")
            break

        print("\n" + "-" * 55)
        while True:
            play_again = input("Хотите сыграть ещё раз? (y/n): ").strip().lower()
            if play_again in ['y', 'н', 'yes', 'да']:
                break
            elif play_again in ['n', 'т', 'no', 'нет']:
                print("\nСпасибо за игру! До свидания!")
                return
            else:
                print("Пожалуйста, введите 'y' (да) или 'n' (нет)")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nИгра прервана пользователем. До новых встреч!")
        sys.exit(0)

#Также добавлена функция вывода загаданного слова, если человек сдался