"""Geohash helper functions"""

import re
from typing import TYPE_CHECKING, Tuple

import libgeohash as gh
from pydantic import (
    ConstrainedFloat,
    ConstrainedInt,
    ConstrainedStr,
    validate_arguments,
)


if TYPE_CHECKING:
    Geohash = str
    GeoPrecision = int
    Latitude = float
    Longitude = float
else:

    class GeoPrecision(ConstrainedInt):
        ge = 1
        le = 12

    class Geohash(ConstrainedStr):
        regex = re.compile(
            rf"^[{gh.geohash_base._base32}]{{{GeoPrecision.ge},{GeoPrecision.le}}}$"
        )

    class Latitude(ConstrainedFloat):
        ge = -90
        le = 90

    class Longitude(ConstrainedFloat):
        ge = -180
        le = 180


Coordinates = Tuple[Latitude, Longitude]


@validate_arguments
def encode(lat: Latitude, lon: Longitude, precision: GeoPrecision) -> str:
    """Obtain geohash encoding of a GPS coordinate"""
    return gh.encode(lat, lon, precision)


@validate_arguments
def decode(geohash: Geohash) -> Coordinates:
    """Decode a geohash into its (lat, lon) coordinates"""
    return gh.decode(geohash)
