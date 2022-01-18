import os
import urllib.request

from tqdm import tqdm

from definitions.defaults import DEFAULT_TEMP_FOLDER, DEFAULT_TILE_SERVER, DEFAULT_IMG_DOWNLOAD_FORMAT
from util import GridBoundingBox, GridIndex


class TileDownloader:
    def __init__(self, tile_servers=None, temp_folder=None, img_format=None):
        self.tile_servers = tile_servers if tile_servers is not None else DEFAULT_TILE_SERVER
        self.temp_folder = temp_folder if temp_folder is not None else DEFAULT_TEMP_FOLDER
        self.img_format = img_format if img_format is not None else DEFAULT_IMG_DOWNLOAD_FORMAT

    def generate_tile_name(self, index: GridIndex):
        return "{}z={}_x={}_y={}.{}".format(self.temp_folder, index.x, index.y, index.z, self.img_format)

    def generate_tile_url(self, index: GridIndex, subserver_index):
        return self.tile_servers[subserver_index].format(x=index.x, y=index.y, z=index.z)

    def download_tiles(self, grid_bb: GridBoundingBox):
        os.makedirs(self.temp_folder, exist_ok=True)
        print("Downloading {} tiles to disk..".format(grid_bb.covered_cells))
        for x, y in tqdm([(x, y) for x in grid_bb.x_range for y in grid_bb.y_range]):
            # download tile x,y,z
            tile_cell = GridIndex(x, y, grid_bb.z)
            url = self.generate_tile_url(tile_cell, 0)
            file_name = self.generate_tile_name(tile_cell)
            _download_tile(url, file_name)
        print()


def _download_tile(url, file_path):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}

    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    data = response.read()

    with open(file_path, 'wb') as f:
        f.write(data)
