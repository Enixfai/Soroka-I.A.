def main():
    try:
        # Ввод количества элементов
        n = int(input("Введите количество чисел (N): "))

        numbers = []
        print(f"Введите {n} целых чисел:")
        for i in range(n):
            num = int(input(f"Число {i + 1}: "))
            numbers.append(num)

        # Обработка последовательности
        sum_squares = 0
        for x in numbers:
            if x < 0:
                sum_squares += x**2  # Возведение в квадрат и добавление к сумме

        # Вывод результата
        print(f"Сумма квадратов отрицательных чисел: {sum_squares}")

    except ValueError:
        print("Ошибка: введено не целое число.")


if __name__ == "__main__":
    main()
