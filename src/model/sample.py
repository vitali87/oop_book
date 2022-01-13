import abc
import random
from typing import Optional, List, overload, Iterable, TypedDict

from src.model.testing_known_sample import TestingKnownSample
from src.model.training_known_sample import TrainingKnownSample


class Sample:
    def __init__(
            self,
            sepal_length: float,
            sepal_width: float,
            petal_length: float,
            petal_width: float,
            species: Optional[str] = None,
    ) -> None:
        self.sepal_length = sepal_length
        self.sepal_width = sepal_width
        self.petal_length = petal_length
        self.petal_width = petal_width
        self.species = species
        self.classification: Optional[str]# = None

    def __repr__(self) -> str:
        known_unknown = "UnknownSample" if self.species is None else "KnownSample"
        classification = "" if self.classification is None else f", {self.classification}"
        return (
            f"{known_unknown}("
            f"sepal_length = {self.sepal_length},"
            f"sepal_width = {self.sepal_width},"
            f"petal_length = {self.petal_length},"
            f"petal_width = {self.petal_width},"
            f"species = {self.species!r}"
            f"{classification}"
            f")"
        )
    def classify(self, classification: str) -> None:
        self.classification = classification
    def matches(self) -> bool:
        return self.species == self.classification

class SampleDict(TypedDict):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str
        

class SamplePartition(List[SampleDict],abc.ABC):
    @overload
    def __init__(self,*,training_subset: float = 0.8) -> None:
        ...

    @overload
    def __init__(
            self,
            iterable: Optional[Iterable[SampleDict]] = None,
            *,
            training_subset: float = 0.8
    ) -> None:
        ...

    def __init__(
            self,
            iterable: Optional[Iterable[SampleDict]] = None,
            *,
            training_subset: float = 0.8,
    ) -> None:
        self.training_subset = training_subset
        if iterable:
            super().__init__(iterable)
        else:
            super().__init__()

    @property
    @abc.abstractmethod
    def training(self) -> List[TrainingKnownSample]:
        ...

    @property
    @abc.abstractmethod
    def testing(self) -> List[TestingKnownSample]:
        ...


class ShuffleSamplePartition(SamplePartition):
    """Shuffle and cut the list into Training and Testing"""

    def __init__(
            self,
            iterable: Optional[Iterable[SampleDict]] = None,
            *,
            training_subset: float = 0.8,
    ) -> None:
        """Constructor for ShuffleSamplePartition"""
        super().__init(
            iterable,
            training_subset=training_subset
        )
        self.split: Optional[int] = None

    def shuffle(self) -> None:
        """"""
        if not self.split:
            random.shuffle(self)
            self.split = int(len(self) * self.training_subset)

    @property
    def training(self) -> List[TrainingKnownSample]:
        self.shuffle()
        return [TrainingKnownSample(**sd) for sd in self[: self.split]]

    @property
    def testing(self) -> List[TestingKnownSample]:
        self.shuffle()
        return [TestingKnownSample(**sd) for sd in self[: self.split]]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"