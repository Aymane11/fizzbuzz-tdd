from abc import ABC
from typing import List
from .utils import ListFactory


class FizzBuzzEngine:
    @staticmethod
    def fizzbuzz(number: int) -> List[str]:
        return [
            FizzBuzzConverter.convert(i)
            for i in ListFactory.create_list(number)
        ]


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
