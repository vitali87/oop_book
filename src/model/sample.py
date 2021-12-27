from typing import Optional


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
        if self.species is None:
            known_unknown = "UnknownSample"
        else:
            known_unknown = "KnownSample"
        if self.classification is None:
            classification = ""
        else:
            classification = f", {self.classification}"
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



