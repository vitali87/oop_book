import csv
import datetime
import json
import logging
import pickle
from pathlib import Path
from threading import Timer
from typing import Any, Iterator
from urllib.request import urlopen

import jsonschema

src_path = Path.cwd()

some_data = [
    "a list", "containing", 5, "items",
    {"including": ["str", "int", "dict"]}
]

with open(src_path / "pickled_list", "wb") as file_write:
    pickle.dump(some_data, file_write)

with open(src_path / "pickled_list", "rb") as file_read:
    loaded_file = pickle.load(file_read)

assert some_data == loaded_file


class URLPolling:
    """
    loads the contents of a web page every hour to ensure that they
    stay up to date
    """

    def __init__(
            self,
            url: str

    ) -> None:
        """Constructor for URLPolling"""
        self.url = url
        self.contents = ""
        self.last_updated: datetime.datetime
        self.timer: Timer
        self.update()

    def update(self) -> None:
        """Responsible for """
        self.contents = urlopen(self.url).read()
        self.last_updated = datetime.datetime.now()
        self.schedule()

    def schedule(self) -> None:
        """Responsible for """
        self.timer = Timer(3600, self.update)
        self.timer.daemon = True
        self.timer.start()

    def __getstate__(self) -> dict[str, Any]:
        pickleable_state = self.__dict__.copy()
        if "timer" in pickleable_state:
            del pickleable_state["timer"]
        return pickleable_state

    def __setstate__(self, pickleable_state: dict[str, Any]) -> None:
        self.__dict__ = pickleable_state
        self.schedule()


class CSVIrisReader():
    """
    Attribute Information:
        1. sepal length in cm
        2. sepal width in cm
        3. petal length in cm
        4. petal width in cm
        5. class:
        -- Iris Setosa
        -- Iris Versicolour
        -- Iris Virginica
    """
    header = [
        "sepal_length",  # in cm
        "sepal_width",  # in cm
        "petal_length",  # in cm
        "petal_width",  # in cm
        "species",  # Iris-setosa, Iris-versicolour, Iris-virginica
    ]

    def __init__(
            self,
            source: Path
    ) -> None:
        """Constructor for CSVIrisReader"""
        self.source = source

    def data_iter(self, ) -> Iterator[dict[str, str]]:
        """Responsible for """

        with self.source.open() as source_file:
            yield from csv.DictReader(source_file, self.header)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"


class CSVIrisReader2():
    '''
    Attribute Information:
        1. sepal length in cm
        2. sepal width in cm
        3. petal length in cm
        4. petal width in cm
        5. class:
            -- Iris Setosa
            -- Iris Versicolour
            -- Iris Virginica
    '''

    def __init__(
            self,
            source: Path
    ) -> None:
        """
        Constructor for CSVIrisReader2
        """
        self.source = source

    def data_iter(self) -> Iterator[dict[str, str]]:
        '''
        Responsible for  yields individual dictionary objects
        '''
        with self.source.open() as source_file:
            reader = csv.reader(source_file)
            for row in reader:
                yield dict(
                    sepal_length=row[0],
                    sepal_width=row[1],
                    petal_length=row[2],
                    petal_width=row[3],
                    species=row[4]
                )

    @property
    def source(self) -> Path:
        '''
        Responsible for docstring_property
        '''
        return self.source

    @property.setter
    def source(self, value):
        '''
        Responsible for setting value of source
        '''
        self.source = value

    @property.deleter
    def source(self):
        '''
        Responsible for deleting source
        '''
        print('Deleting f"self.source"')
        del self.source

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}"


from typing import TypedDict


class SampleDict(TypedDict, total=True):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str


class JSONIrisReader:
    def __init__(self, source: Path) -> None:
        self.source = source

    def data_iter(self) -> Iterator[SampleDict]:
        with self.source.open() as source_file:
            sample_list = json.load(source_file)
        yield from iter(sample_list)


class NDJSONIrisReader:
    def __init__(self, source: Path) -> None:
        self.source = source

    def data_iter(self) -> Iterator[SampleDict]:
        with self.source.open() as source_file:
            for line in source_file:
                sample = json.loads(line)
            yield sample


IRIS_SCHEMA = {
    "$schema": "https://json-schema.org/draft/2019-09/hyper-schema",
    "title": "Iris Data Schema",
    "description": "Schema of Bezdek Iris data",
    "type": "object",
    "properties": {
        "sepal_length": {
            "type": "number", "description": "Sepal Length in cm"},
        "sepal_width": {
            "type": "number", "description": "Sepal Width in cm"},
        "petal_length": {
            "type": "number", "description": "Petal Length in cm"},
        "petal_width": {
            "type": "number", "description": "Petal Width in cm"},
        "species": {
            "type": "string",
            "description": "class",
            "enum": [
                "Iris-setosa", "Iris-versicolor", "Iris-virginica"],
        },
    },
    "required": [
        "sepal_length", "sepal_width", "petal_length", "petal_width"],
}


class ValidatingNDJSONIrisReader:
    def __init__(self, source: Path, schema: dict[str, Any]) -> None:
        self.source = source
        self.validator = jsonschema.Draft7Validator(schema)

    def data_iter(self) -> Iterator[SampleDict]:
        with self.source.open() as source_file:
            for line in source_file:
                sample = json.loads(line)
                if self.validator.is_valid(sample):
                    yield sample
                else:
                    logging.error(f'Invalid {sample}')
