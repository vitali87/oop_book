from enum import Enum
from typing import Set


class Species(Enum):
    Setosa = "Iris-setosa"
    Versicolour = "Iris-versicolour"
    Virginica = "Iris-virginica"


class Domain(Set[str]):
    def validate(self, value: str) -> str:
        if value in self:
            return value
        raise ValueError(f"invalid {value!r}")
