import math


class Point:
    """
    Representing a point in two-dimensional
    coordinate system

    >>> p_0 = Point()
    >>> p_1 = Point(3, 4)
    >>> p_0.calculate_distance(p_1)
    5.0
    """

    def __init__(self, x: float = 0, y: float = 0) -> None:
        '''
        Initialise the position of a new point. The x and y
        coordinates can be specified. If they are not, the
        point defaults to the origin.

        :param x: float x-coordinate
        :param y: float y-coordinate
        '''
        self.move(x, y)

    def move(self, x: float, y: float) -> None:
        '''
        Move the point to a new location in two-dimensional
        space.

        :param x: float x-coordinate
        :param y: float y-coordinate
        '''
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        Reset the point to the origin: 0,0
        :return:
        """
        self.move(0, 0)

    def move(self, x: float, y: float) -> None:
        """
        Move the point to a new location
        in two-dimensional space.

        :param
        x: float
        x - coordinate
        :param
        y: float
        y - coordinate
        """
        self.x = x
        self.y = y

    def reset(self) -> None:
        """
        Reset the point to the origin: 0, 0
        """

        self.move(0, 0)

    def calculate_distance(self, p: "Point") -> float:
        """
        Calculate the Euclidean distance between
        this point and the second point passed as a
        parameter.

        :param
        p: Point instance
        :return float distance
        """
        return math.hypot(self.x - p.x, self.y - p.y)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
