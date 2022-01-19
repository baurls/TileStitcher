# main file for staring / experimenting
from util import conversion, Coordinate, GridBoundingBox
from util.tile_loader import TileDownloader
from util.tile_merger import TileMerger

start = Coordinate(48.139974, 9.20929)  # lat, lon
end = Coordinate(48.111443, 9.271603)  # lat, lon

zoom = 17

start_grid_index = conversion.get_index_from_coordinate(start, zoom)
end_grid_index = conversion.get_index_from_coordinate(end, zoom)

grid_bb = GridBoundingBox(start_grid_index, end_grid_index)

print(grid_bb)

#  download images
downloader = TileDownloader()
downloader.download_tiles(grid_bb)

# merge image
merger = TileMerger()
merger.merge(grid_bb)
