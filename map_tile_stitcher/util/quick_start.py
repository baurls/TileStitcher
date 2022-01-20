from map_tile_stitcher import TileDownloader, TileMerger, Coordinate, GridBoundingBox
from map_tile_stitcher.util import conversion


class QuickMapStitcher:
    def __init__(self, downloader: TileDownloader = None, merger: TileMerger = None):
        if downloader is None:
            downloader = TileDownloader()
            self.downloader = downloader

        if merger is None:
            merger = TileMerger()
            self.merger = merger

    def download_and_stitch(self, start: Coordinate, end: Coordinate, zoom: int):
        # convert lon-lat coordinates to grid-cell indices
        start_grid_index = conversion.get_index_from_coordinate(start, zoom)
        end_grid_index = conversion.get_index_from_coordinate(end, zoom)

        # set up request bounding box
        grid_bb = GridBoundingBox(start_grid_index, end_grid_index)

        # download images
        self.downloader.download_tiles(grid_bb)

        # merge image
        self.merger.merge(grid_bb)


