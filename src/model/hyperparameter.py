import weakref
from typing import Optional


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

