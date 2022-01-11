from typing import List


class AverageList(List[int]):
    @property
    def average(self) -> float:
        return sum(self)/ len(self)
