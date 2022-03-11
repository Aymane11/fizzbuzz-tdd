from abc import ABC
from typing import List


class FizzBuzzEngine:
    @staticmethod
    def fizzbuzz(number: int) -> List[str]:
        pass


class FizzBuzzConverter(ABC):
    @staticmethod
    def convert(number: int) -> str:
        if number % 3 == 0 and number % 5 == 0:
            return "FizzBuzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        return str(number)
