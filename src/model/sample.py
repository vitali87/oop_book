import abc
import csv
import enum
import random
import weakref
from datetime import datetime
from enum import Enum
from pathlib import Path
from typing import Optional, List, overload, Iterable, TypedDict, Set, Iterator

from src.own_exceptions import InvalidSampleError, BadSampleRow


class Species(Enum):
    Setosa = "Iris-setosa"
    Versicolour = "Iris-versicolour"
    Virginica = "Iris-virginica"


class Domain(Set[str]):
    def validate(self, value: str) -> str:
        if value in self:
            return value
        raise ValueError(f"invalid {value!r}")


species = Domain({"Iris-setos","Iris-versicolour","Irsi-virginica"})


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


class Hyperparameter:
    """ A hyperparameter value and overall quality of
    the classification
    """

    def __init__(self, k: int, training: 'TrainingData') -> None:
        self.k = k
        self.data: weakref.ReferenceType['TrainingData'] = weakref.ref(training)
        self.quality: float

    def test(self) -> None:
        """ Run the entire test suite."""
        training_data: Optional["TrainingData"] = self.data()
        if not training_data:
            raise RuntimeError("Broken Weak Reference")
        pass_count, fail_count = 0,0
        for sample in training_data.testing:
            sample.classification = self.classify(sample)
            if sample.matches():
                pass_count += 1
            else:
                fail_count += 1
        self.quality = pass_count/(pass_count + fail_count)


class TrainingData:
    """A set of training data and testing
    data with methods load and test the samples"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.uploaded: datetime.datetime
        self.tested: datetime.datetime
        self.training: List[TrainingKnownSample2] = []
        self.testing: List[TestingKnownSample] = []
        self.tuning: List[Hyperparameter] = []

    def load(self, raw_data_iter: Iterable[dict[str,str]]) -> None:
        """Load and split raw data"""
        bad_count = 0
        for n, row in enumerate(raw_data_iter):
            try:
                if n % 5 == 0:
                    test = TestingKnownSample.from_dict(row)
                    self.testing.append(test)
                else:
                    train = TrainingKnownSample2.from_dict(row)
                    self.training.append(train)
            except InvalidSampleError as ex:
                print(f"Row {n+1}: {ex}")
                bad_count += 1
        if bad_count != 0:
            print(f"{bad_count} invalid rows")
            return
        self.uploaded = datetime.datetime.now(tz=datetime.timezone.utc)

    def test(self,parameter: Hyperparameter) -> None:
        """Test this Hyperparameter value"""
        parameter.test()
        self.tuning.append(parameter)
        self.tested = datetime.datetime.now(tz=datetime.timezone.utc)

    def classify(self,
                 parameter: Hyperparameter,
                 sample: Sample) -> None:
        """Classify this Sample"""
        classification = parameter.classify(sample)
        sample.classify(classification)
        return sample


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


class TestingKnownSample(KnownSample):
    pass
    # @classmethod
    # def from_dict(cls, row: dict[str, str]eks = TrainingKnownSample2(valid)) -> "TrainingKnownSample":
    #     return cast(TrainingKnownSample, super().from_dict(row))


class TrainingKnownSample(KnownSample):
    pass
    # @classmethod
    # def from_dict(cls, row: dict[str, str]) -> "TrainingKnownSample":
    #     return cast(TrainingKnownSample, super().from_dict(row))


class TrainingKnownSample2(KnownSample2):
    pass
    # @classmethod
    # def from_dict(cls, row: dict[str, str]) -> "TrainingKnownSample":
    #     return cast(TrainingKnownSample, super().from_dict(row))


class SampleReader:
    """
    See iris.names for attribute ordering in bezdekIris.data file
    """

    target_class = Sample
    header = [
        "sepal_length", "sepaal_width",
        "petal_length", "petal_width"
    ]

    def __init__(self,source: Path) -> None:
        self.source = source

    def sample_iter(self) -> Iterator[Sample]:
        target_class = self.target_class
        with self.source.open() as source_file:
            reader = csv.DictReader(source_file,self.header)
            for row in reader:
                try:
                    sample = target_class(
                        sepal_length=float(row["sepal_length"]),
                        sepal_width=float(row["sepal_width"]),
                        petal_length=float(row["petal_length"]),
                        petal_width=float(row["petal_width"]),
                    )
                except ValueError as ex:
                    raise BadSampleRow(f"Invalid {row!r}") from ex
                yield sample


class Purpose(enum.IntEnum):
    Classification = 0
    Testing = 1
    Training = 2


class SampleDict(TypedDict):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str
        

class SamplePartition(List[SampleDict],abc.ABC):
    @overload
    def __init__(self, *, training_subset: float = 0.8) -> None:
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


class ShufflingSamplePartition(SamplePartition):
    """Shuffle and cut the list into Training and Testing"""

    def __init__(
            self,
            iterable: Optional[Iterable[SampleDict]] = None,
            *,
            training_subset: float = 0.8,
    ) -> None:
        """Constructor for ShuffleSamplePartition"""
        super().__init__(
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


