from abc import ABC


class FizzBuzzEngine:
    pass


class FizzBuzzConverter(ABC):
    @staticmethod
    def convert(number: int) -> str:
        if number == 1:
            return "1"
        return "Fizz"
