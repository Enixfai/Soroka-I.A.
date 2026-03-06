from abc import ABC, abstractmethod


class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, num):
        self.value += num
        return self.value

    def subtract(self, num):
        self.value -= num
        return self.value

    def multiply(self, num):
        self.value *= num
        return self.value

    def divide(self, num):
        if num == 0:
            raise ValueError("Деление на ноль!")
        self.value /= num
        return self.value

    def reset(self):
        self.value = 0
        return self.value


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class AddCommand(Command):
    def __init__(self, calculator, num):
        self.calculator = calculator
        self.num = num

    def execute(self):
        return self.calculator.add(self.num)


class SubtractCommand(Command):
    def __init__(self, calculator, num):
        self.calculator = calculator
        self.num = num

    def execute(self):
        return self.calculator.subtract(self.num)


class MultiplyCommand(Command):
    def __init__(self, calculator, num):
        self.calculator = calculator
        self.num = num

    def execute(self):
        return self.calculator.multiply(self.num)


class DivideCommand(Command):
    def __init__(self, calculator, num):
        self.calculator = calculator
        self.num = num

    def execute(self):
        return self.calculator.divide(self.num)


class ResetCommand(Command):
    def __init__(self, calculator):
        self.calculator = calculator

    def execute(self):
        return self.calculator.reset()


class Button:
    def __init__(self, command=None):
        self.command = command

    def set_command(self, command):
        self.command = command

    def press(self):
        if self.command:
            return self.command.execute()
        raise ValueError("Команда не назначена")


if __name__ == "__main__":
    calc = Calculator()

    add5 = Button(AddCommand(calc, 5))
    sub2 = Button(SubtractCommand(calc, 2))
    reset = Button(ResetCommand(calc))

    print("Добавляем 5:", add5.press())
    print("Вычитаем 2:", sub2.press())

    custom = Button()
    custom.set_command(MultiplyCommand(calc, 10))
    print("Умножаем на 10:", custom.press())

    custom.set_command(DivideCommand(calc, 3))
    print("Делим на 3:", custom.press())
