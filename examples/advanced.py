# main file for staring / experimenting
from map_tile_stitcher.util import conversion
from map_tile_stitcher.util.data_structures import Coordinate, GridBoundingBox
from map_tile_stitcher.util.tile_loading import TileDownloader
from map_tile_stitcher.util.tile_merging import TileMerger

import logging

logging.basicConfig(level=logging.INFO)

# define your requesting area and resolution
start = Coordinate(48.139974, 9.20929)  # lat, lon
end = Coordinate(48.111443, 9.271603)  # lat, lon
zoom = 16  # from range 1..18, where 1 is course and 18 is very high-detail

# convert lon-lat coordinates to grid-cell indices
start_grid_index = conversion.get_index_from_coordinate(start, zoom)
end_grid_index = conversion.get_index_from_coordinate(end, zoom)

# set up request bounding box
grid_bb = GridBoundingBox(start_grid_index, end_grid_index)

# download images
downloader = TileDownloader()
downloader.download_tiles(grid_bb)

# merge image
merger = TileMerger()
merger.merge(grid_bb)
