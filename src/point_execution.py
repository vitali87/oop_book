class Point:
    """
    Represents a point in two-dimensional geometric coordinates
    """
    pass


def main() -> None:
    """
    Does the usefule work.
    
    >>> main()
    p1.calculate_distance(p2) = 5
    """
    p1 = Point()
    p2 = Point(3, 4)
    print(f"{p1.calculate_distance(p2)=}")


if __name__ == "__main__":
    main()
