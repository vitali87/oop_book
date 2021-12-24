from src.model.sample import Sample
from math import hypot

class Distance:
    """Definition of a ditance computation"""
    def distance(self,s1: Sample,s2: Sample) -> float:
        pass

# Euclidean distance
class ED(Distance):
    def distance(self,s1: Sample,s2: Sample) -> float:
        return hypot(
            s1.sepal_length - s2.sepal_length,
            s1.sepal_width - s2.sepal_width,
            s1.petal_length - s2.petal_length,
            s1.petal_width - s2.petal_width,
        )

# Manhattan distance
class MD(Distance):
    def distance(self,s1: Sample,s2: Sample) -> float:
        return sum([
            abs(s1.sepal_length - s2.sepal_length),
            abs(s1.sepal_width - s2.sepal_width),
            abs(s1.petal_length - s2.petal_length),
            abs(s1.petal_width - s2.petal_width),
            ]
        )

# Chebyshev distance
class CD(Distance):
    def distance(self,s1: Sample,s2: Sample) -> float:
        return max([
            abs(s1.sepal_length - s2.sepal_length),
            abs(s1.sepal_width - s2.sepal_width),
            abs(s1.petal_length - s2.petal_length),
            abs(s1.petal_width - s2.petal_width),
            ]
        )

# Sorensen distance
class SD(Distance):
    def distance(self,s1: Sample,s2: Sample) -> float:
        return sum([
            abs(s1.sepal_length - s2.sepal_length),
            abs(s1.sepal_width - s2.sepal_width),
            abs(s1.petal_length - s2.petal_length),
            abs(s1.petal_width - s2.petal_width),
            ]
        )/ sum([
            abs(s1.sepal_length + s2.sepal_length),
            abs(s1.sepal_width + s2.sepal_width),
            abs(s1.petal_length + s2.petal_length),
            abs(s1.petal_width + s2.petal_width),
            ]
        )