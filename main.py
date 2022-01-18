# main file for staring / experimenting

from util import conversion

TILE_SERVERS = {
    "OSM_STANDARD" : [
                "http://a.tile.openstreetmap.org/{z}/{x}/{y}.png",
                "http://b.tile.openstreetmap.org/{z}/{x}/{y}.png",
                "http://c.tile.openstreetmap.org/{z}/{x}/{y}.png"
    ]
}

start = (48.139974, 9.20929)  # lat, lon
end = (48.111443, 9.271603)  # lat, lon

zoom = 2

print(start)
print(end)

temp_start_x, temp_start_y = conversion.get_index_from_coordinate(start[1], start[0], zoom)
temp_end_x, temp_end_y = conversion.get_index_from_coordinate(end[1], end[0], zoom)

print(temp_start_x, temp_start_y)
print(temp_end_x, temp_end_y )

start_x = min(temp_end_x, temp_start_x)
end_x = max(temp_end_x, temp_start_x)
start_y = min(temp_start_y, temp_end_y)
end_y = max(temp_start_y, temp_end_y)

print(start_x, start_y)
print(end_x, end_y)

tiles = (end_x - start_x + 1) * (end_y - start_y + 1)
print(tiles)

import urllib.request

def download_image(url, file_path):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent}

    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    data = response.read()

    print(type(data))

    with open(file_path, 'wb') as f: f.write(data)


#  download images

TEMP_FOLDER = "_tile_cache/"
OUT_FOLDER = "./"
import os

def get_tilename(x, y, zoom, img_format=".png"):
    filename = TEMP_FOLDER + "z={}_x={}_y={}.{}".format(x, y, zoom, img_format)
    return filename

os.makedirs(TEMP_FOLDER, exist_ok=True)

tile_server_template = TILE_SERVERS["OSM_STANDARD"][0]

x_range = range(start_x, end_x + 1)
y_range = range(start_y, end_y + 1)

for x in x_range:
    for y in y_range:
        # download tile x,y,z
        url = tile_server_template.format(x=x, y=y, z=zoom)
        filename = get_tilename(x, y, zoom)
        print("Downloading: " + url)
        download_image(url, filename)



# stick images together
start_file = get_tilename(x_range[0], y_range[0], zoom)

# (1) extract size from first image
from PIL import Image
start_image = Image.open(start_file)
img_size = start_image.size
assert img_size[0] == img_size[1], "Tiles must be quadratic. This tile, however, is rectangular: {}".format(img_size)

tile_size = img_size[0]
print(tile_size)

# (2) stick together

merged_image = Image.new('RGB', (len(x_range) * tile_size, len(y_range) * tile_size))
for i, x in enumerate(x_range):
    for j, y in enumerate(y_range):
        current_tile = Image.open(get_tilename(x,y,zoom))
        merged_image.paste(current_tile,(tile_size*i,tile_size*j))

IMG_FORMAT_PNG = ("png", "PNG")
IMG_FORMAT_JPG = ("jpg", "JPEG")
img_format = IMG_FORMAT_PNG
img_name = "map_z{z}_x{x1}-{x2}_y{y1}-{y2}".format(z=zoom, x1=start_x, x2=end_x, y1=start_y, y2=end_y)
os.makedirs(OUT_FOLDER, exist_ok=True)
merged_image.save("{}{}.{}".format(OUT_FOLDER, img_name, img_format[0]),img_format[1])