from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def prepare(self):
        pass


class Espresso(Coffee):
    def prepare(self):
        return "Готовим эспрессо"


class Americano(Coffee):
    def prepare(self):
        return "Готовим американо"


class Cappuccino(Coffee):
    def prepare(self):
        return "Готовим капучино"


class Latte(Coffee):
    def prepare(self):
        return "Готовим латте"


class Mocha(Coffee):
    def prepare(self):
        return "Готовим мокко"


class CoffeeMachine:
    def create_coffee(self, coffee_type: str) -> Coffee:
        if coffee_type == "1":
            return Espresso()
        if coffee_type == "2":
            return Americano()
        if coffee_type == "3":
            return Cappuccino()
        if coffee_type == "4":
            return Latte()
        if coffee_type == "5":
            return Mocha()

        raise ValueError("Неверный выбор напитка")

    def order_coffee(self, coffee_type: str):
        coffee = self.create_coffee(coffee_type)
        print(coffee.prepare())


def show_menu():
    print("\n===  КОФЕ-АВТОМАТ ===")
    print("1 — Эспрессо")
    print("2 — Американо")
    print("3 — Капучино")
    print("4 — Латте")
    print("5 — Мокко")
    print("0 — Выход")


def main():
    machine = CoffeeMachine()

    while True:
        show_menu()
        choice = input("Выберите напиток: ").strip()

        if choice == "0":
            print("До свидания!")
            break

        try:
            machine.order_coffee(choice)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()
