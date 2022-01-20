# main file for staring / experimenting
from tile_stitcher.util import conversion
from tile_stitcher.util.data_structures import Coordinate, GridBoundingBox
from tile_stitcher.util.tile_loading import TileDownloader
from tile_stitcher.util.tile_merging import TileMerger

start = Coordinate(48.139974, 9.20929)  # lat, lon
end = Coordinate(48.111443, 9.271603)  # lat, lon

zoom = 17
import logging

logging.basicConfig(level=logging.INFO)

start_grid_index = conversion.get_index_from_coordinate(start, zoom)
end_grid_index = conversion.get_index_from_coordinate(end, zoom)

grid_bb = GridBoundingBox(start_grid_index, end_grid_index)

#  download images
downloader = TileDownloader()
downloader.download_tiles(grid_bb)

# merge image
merger = TileMerger()
merger.merge(grid_bb)
