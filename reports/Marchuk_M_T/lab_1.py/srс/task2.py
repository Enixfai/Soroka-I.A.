"""
Модуль для поиска индексов двух чисел, сумма которых равна целевому числу.

Пользователь вводит список чисел и целевое значение.
Программа возвращает индексы элементов.
"""


def find_two_sum(nums: list[int], target: int) -> list[int]:
    """
    Ищет индексы двух чисел, сумма которых равна target.

    :param nums: Список целых чисел
    :param target: Целевое число
    :return: Список из двух индексов
    """
    prev_map = {}  # значение : индекс

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prev_map:
            return [prev_map[diff], i]
        prev_map[n] = i

    return []


def main() -> None:
    """
    Точка входа в программу.
    """
    try:
        user_input = input("Введите список чисел nums через пробел: ")
        nums = list(map(int, user_input.split()))
        target = int(input("Введите целевое число target: "))

        result = find_two_sum(nums, target)
        print(f"Output: {result}")
    except ValueError:
        print("Ошибка: вводите только целые числа.")


if __name__ == "__main__":
    main()
