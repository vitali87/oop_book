from math import radians, pi, hypot, cos


def distance(
        lat1: float, lon1: float, lat2: float, lon2: float
) -> float:
    d_lat = radians(lat2) - radians(lat1)
    d_lon = min(
        (radians(lon2) - radians(lon1) % (2 * pi)),
        (radians(lon1) - radians(lon2) % (2 * pi)),
    )
    R = 60 * 180 / pi
    return hypot(R * d_lat, R * cos(radians(lat1)) * d_lon)
