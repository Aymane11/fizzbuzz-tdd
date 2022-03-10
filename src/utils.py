from abc import ABC
from typing import List

class ListFactory(ABC):
    @staticmethod
    def create_list(n: int) -> List[int]:
        if n <= 0:
            raise ValueError("n must be greater than 0")
        return list(range(1, n + 1))