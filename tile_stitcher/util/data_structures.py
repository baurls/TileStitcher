class Coordinate:

    def __init__(self, lat: float, lon: float):
        """
        Coordinate object
        :param lat: latitude value (in range [-90°, 90°] )
        :param lon: longitude value (in range [-180°, 180°] )
        """
        assert -90 <= lat <= 90
        assert -180 <= lon <= 180
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return "({lat}, {lon})".format(lat=self.lat, lon=self.lon)

    def __repr__(self):
        return str(self)


class GridIndex:
    def __init__(self, x: int, y: int, z: int):
        assert z >= 0
        assert 0 <= x < 2 ** z
        assert 0 <= y < 2 ** z
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return "({z}, {x}, {y})".format(z=self.z, x=self.x, y=self.y)

    def __repr__(self):
        return str(self)


class GridBoundingBox:
    def __init__(self, cell1: GridIndex, cell2: GridIndex):
        assert cell1.z == cell2.z, "Can't calculate a grid on different scales yet"
        start_x = min(cell1.x, cell2.x)
        end_x = max(cell1.x, cell2.x)
        start_y = min(cell1.y, cell2.y)
        end_y = max(cell1.y, cell2.y)
        self.z = cell1.z
        self.lower_corner = GridIndex(start_x, start_y, z=self.z)
        self.upper_corner = GridIndex(end_x, end_y, z=self.z)

    @property
    def covered_cells(self):
        return (self.upper_corner.x - self.lower_corner.x + 1) * (self.upper_corner.y - self.lower_corner.y + 1)

    @property
    def x_range(self):
        return range(self.lower_corner.x, self.upper_corner.x + 1)

    @property
    def y_range(self):
        return range(self.lower_corner.y, self.upper_corner.y + 1)

    def __str__(self):
        return "[{p1}x{p2}]".format(p1=self.lower_corner, p2=self.upper_corner)

    def __repr__(self):
        return str(self)