# Задача о лестнице (аналог чисел Фибоначчи)


def climb_stairs():
    try:
        n = int(input("Введите количество ступенек (n): "))

        if n <= 0:
            print("Количество ступенек должно быть положительным числом.")
            return

        # Базовые случаи:
        # Если 1 ступенька — 1 способ
        # Если 2 ступеньки — 2 способа (1+1 или 2)
        if n == 1:
            print("Количество способов: 1")
            return
        if n == 2:
            print("Количество способов: 2")
            return

        # Итеративный расчет (оптимально по памяти)
        prev2 = 1  # Способы для (n-2)
        prev1 = 2  # Способы для (n-1)
        current = 0

        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        print(f"Количество способов: {current}")

    except ValueError:
        print("Ошибка: введите целое число.")


if __name__ == "__main__":
    climb_stairs()
