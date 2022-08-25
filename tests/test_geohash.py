import pytest

from project.geohash import (
    Coordinates,
    Geohash,
    GeoPrecision,
    Latitude,
    Longitude,
    decode,
    encode,
)


@pytest.mark.parametrize(
    "lat, lon, geohash12",
    [(38.89768, -77.03653, "dqcjqcpeqtpg"), (40.68925, -74.04450, "dr5r7p62n1gn")],
)
class TestGeohash:
    """Unit tests for encoding and decoding of geohashes"""

    @staticmethod
    def _round(coords: Coordinates) -> Coordinates:
        """Round GPS coordinates to 5 digits"""
        return tuple(round(coord, 5) for coord in coords)  # type: ignore[return-value]

    @pytest.mark.parametrize("precision", range(1, 13))
    def test_encode(
        self,
        lat: Latitude,
        lon: Longitude,
        precision: GeoPrecision,
        geohash12: Geohash,
    ):
        """Unit test for project.encode() function"""
        assert encode(lat, lon, precision) == geohash12[:precision]

    def test_decode(self, lat: Latitude, lon: Longitude, geohash12: Geohash):
        """Unit test for project.decode() function"""
        result = decode(geohash12)
        assert self._round(result) == self._round((lat, lon))
