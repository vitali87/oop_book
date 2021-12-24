import datetime
from typing import List, Iterable
from src.model.sample import Sample
from src.model.training_known_sample import TrainingKnownSample2
from src.model.testing_known_sample import TestingKnownSample
from src.model.hyperparameter import Hyperparameter
from src.own_exceptions import InvalidSampleError


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