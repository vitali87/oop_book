from typing import Optional

from src.model.purpose import Purpose
from src.model.sample import Sample
from src.own_exceptions import InvalidSampleError
from src.model.species import Domain

species = Domain({"Iris-setos","Iris-versicolour","Irsi-virginica"})


class KnownSample(Sample):
    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "KnownSample":
        if row["species"] not in {
                "Iris-setosa", "Iris-versicolour", "Iris-virginica"}:
            raise InvalidSampleError(f"invalid species in {row!r}")
        try:
            return cls(
                species=row["species"],
                sepal_length=float(row["sepal_length"]),
                sepal_width=float(row["sepal_width"]),
                petal_length=float(row["petal_length"]),
                petal_width=float(row["petal_width"])
            )
        except ValueError as ex:
            raise InvalidSampleError(f"invalid {row!r}")

    def __init__(
            self,
            sepal_length: float,
            sepal_width: float,
            petal_length: float,
            petal_width: float,
            species: str
    ) -> None:
        super().__init__(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
        )
        self.species = species

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length = {self.sepal_length},"
            f"sepal_width = {self.sepal_width},"
            f"petal_length = {self.petal_length},"
            f"petal_width = {self.petal_width},"
            f"species = {self.species!r}"
            f")"
        )


class KnownSample2(Sample):
    @classmethod
    def from_dict(cls, row: dict[str, str]) -> "KnownSample2":
        try:
            return cls(
                species=species.validate(row["species"]),
                sepal_length=float(row["sepal_length"]),
                sepal_width=float(row["sepal_width"]),
                petal_length=float(row["petal_length"]),
                petal_width=float(row["petal_width"]),
            )
        except ValueError as ex:
            raise InvalidSampleError(f"invalid {row!r}")

    def __init__(
            self,
            sepal_length: float,
            sepal_width: float,
            petal_length: float,
            petal_width: float,
            species: str
    ) -> None:
        super().__init__(
            sepal_length=sepal_length,
            sepal_width=sepal_width,
            petal_length=petal_length,
            petal_width=petal_width,
        )
        self.species = species

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"sepal_length = {self.sepal_length},"
            f"sepal_width = {self.sepal_width},"
            f"petal_length = {self.petal_length},"
            f"petal_width = {self.petal_width},"
            f"species = {self.species!r}"
            f")"
        )


class KnownSample3(Sample):
    def __init__(
            self,
            sepal_length: float,
            sepal_width: float,
            petal_length: float,
            petal_width: float,
            purpose: int,
            species: str,
    ) -> None:
        purpose_enum = Purpose(purpose)
        if purpose_enum not in {Purpose.Training,Purpose.Testing}:
            raise ValueError(
                f"Invalid purpose: {purpose!r}: {purpose_enum}"
            )
        super().__init__(sepal_length=sepal_length,
                         petal_length=petal_length,
                         sepal_width=sepal_width,
                         petal_width=petal_width,
                         )
        self.purpose = purpose
        self.species = species
        self._classification: Optional[str] = None

    def matches(self) -> bool:
        return self.species == self.classification

    @property
    def classification(self) -> Optional[str]:
        if self.purpose == Purpose.Testing:
            return self._classification
        else:
            raise AttributeError("Training samples have no classification")

    @classification.setter
    def classification(self, value: str) -> None:
        if self.purpose == Purpose.Testing:
            self._classification = value
        else:
            raise AttributeError(
                "Training Samples cannot be classified"
            )
