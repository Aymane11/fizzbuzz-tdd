from abc import ABC


class FizzBuzzEngine:
    pass


class FizzBuzzConverter(ABC):
    @staticmethod
    def convert(number: int) -> str:
        return "1"
