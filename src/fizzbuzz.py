from abc import ABC


class FizzBuzzEngine:
    pass


class FizzBuzzConverter(ABC):
    @staticmethod
    def convert(number: int) -> str:
        if number % 3 != 0 and number % 5 != 0:
            return str(number)
        elif number % 3 == 0:
            return "Fizz"
        else:
            return "Buzz"
