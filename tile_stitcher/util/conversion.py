# This module converts lon-lat requests to the respective tile indices.
# Code taken from https://wiki.openstreetmap.org/wiki/Slippy_map_tilenames
import math

from tile_stitcher.util.data_structures import Coordinate, GridIndex


def get_index_from_coordinate(coordinate: Coordinate, zoom: int) -> GridIndex:
    (x, y) = _get_index_from_coordinate(coordinate.lon, coordinate.lat, zoom)
    return GridIndex(x, y, zoom)


def get_coordinate_from_index(grid_index: GridIndex) -> Coordinate:
    lon, lat = _get_coordinate_from_index(grid_index.x, grid_index.y, grid_index.z)
    return Coordinate(lat, lon)


def _get_index_from_coordinate(lon: float, lat: float, z: int) -> (int, int):
    assert z >= 0, "Level must po positive"
    x = int(((lon + 180) / 360) * (2 ** z))
    scaled_lat = lat * math.pi / 180
    y = int((1 - (math.log(math.tan(scaled_lat) + 1 / math.cos(scaled_lat))) / math.pi) * 2 ** (z - 1))
    return x, y


def _get_coordinate_from_index(x: int, y: int, z: int) -> (float, float):
    assert z >= 0, "Level must po positive"
    divisor = (2 ** z)
    lon = (x / divisor) * 360 - 180
    lat = math.degrees(math.atan(math.sinh(math.pi - (y / divisor) * 2 * math.pi)))
    return lon, lat
