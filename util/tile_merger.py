from PIL import Image
import os
from tqdm import tqdm

from definitions.defaults import DEFAULT_IMG_DOWNLOAD_FORMAT, DEFAULT_OUT_FOLDER, DEFAULT_TEMP_FOLDER, \
    DEFAULT_IMG_STORE_FORMAT
from util import GridBoundingBox, GridIndex


class TileMerger:
    def __init__(self, temp_folder=None, output_folder=None, img_input_format=None, img_output_format=None):
        self.img_input_format = img_input_format if img_input_format is not None else DEFAULT_IMG_DOWNLOAD_FORMAT
        self.img_output_format = img_output_format if img_output_format is not None else DEFAULT_IMG_STORE_FORMAT
        self.output_folder = output_folder if output_folder is not None else DEFAULT_OUT_FOLDER
        self.temp_folder = temp_folder if temp_folder is not None else DEFAULT_TEMP_FOLDER

    @staticmethod
    def _get_output_name(grid_bb: GridBoundingBox) -> str:
        return "map_z{z}_x{x1}-{x2}_y{y1}-{y2}".format(z=grid_bb.z, x1=grid_bb.lower_corner.x,
                                                       x2=grid_bb.upper_corner.x, y1=grid_bb.lower_corner.y,
                                                       y2=grid_bb.upper_corner.y)

    def _generate_tile_name(self, index: GridIndex):
        return "{}z={}_x={}_y={}.{}".format(self.temp_folder, index.x, index.y, index.z, self.img_input_format)

    def _load_image_to_grid_cell(self, cell_index: GridIndex):
        filename = self._generate_tile_name(cell_index)
        image = Image.open(filename)
        return image

    def _load_tile_size(self, grid_bb: GridBoundingBox):
        start_image = self._load_image_to_grid_cell(grid_bb.lower_corner)
        img_size = start_image.size
        assert img_size[0] == img_size[1], "Tiles must be quadratic. This tile, however, is rectangular: {}".format(
            img_size)
        tile_size = img_size[0]
        return tile_size

    def merge(self, grid_bb):

        os.makedirs(self.output_folder, exist_ok=True)

        tile_size = self._load_tile_size(grid_bb)
        merged_image = Image.new('RGB', (len(grid_bb.x_range) * tile_size, len(grid_bb.y_range) * tile_size))

        print("Merging tiles to one file..")
        for i, x in tqdm(enumerate(grid_bb.x_range)):
            for j, y in enumerate(grid_bb.y_range):
                current_cell = GridIndex(x, y, grid_bb.z)
                current_tile = Image.open(self._generate_tile_name(current_cell))
                merged_image.paste(current_tile, (tile_size * i, tile_size * j))

        out_name = self._get_output_name(grid_bb)
        out_filename = "{}{}.{}".format(self.output_folder, out_name, self.img_output_format[0])
        merged_image.save(out_filename, self.img_output_format[1])
        print()
        print("The image has been stored at {}".format(out_filename))
