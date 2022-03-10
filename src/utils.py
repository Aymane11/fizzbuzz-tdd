from abc import ABC
from typing import List

class ListFactory(ABC):
    @staticmethod
    def create_list(n: int) -> List[int]:
        return [1]