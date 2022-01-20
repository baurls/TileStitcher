# main file for staring / experimenting
import logging
logging.basicConfig(level=logging.INFO)

from map_tile_stitcher.util.data_structures import Coordinate
from map_tile_stitcher.util.quick_start import QuickMapStitcher


# define your requesting area and resolution
start = Coordinate(48.139974, 9.20929)  # lat, lon
end = Coordinate(48.111443, 9.271603)  # lat, lon
zoom = 16  # from range 1..18, where 1 is course and 18 is very high-detail

stitcher = QuickMapStitcher()
stitcher.download_and_stitch(start, end, zoom)
