"""
Модуль для проверки равенства всех элементов последовательности.

Запрашивает у пользователя числа, проверяет их на идентичность
и выводит результат: "равны" или "не равны".
"""


def are_elements_equal(numbers: list[int]) -> str:
    """
    Проверяет, все ли элементы в списке одинаковые.

    :param numbers: Список целых чисел
    :return: Строка "равны" или "не равны"
    """
    if not numbers:
        return "пусто"

    if len(set(numbers)) == 1:
        return "равны"

    return "не равны"


def main() -> None:
    """
    Точка входа в программу.
    """
    try:
        user_input = input("Введите числа через пробел: ")
        nums = list(map(int, user_input.split()))
        result = are_elements_equal(nums)
        print(result)
    except ValueError:
        print("Ошибка: вводите только целые числа.")


if __name__ == "__main__":
    main()
