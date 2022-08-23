from PIL import Image
from utils import flatten


def create_image(path, pixel_data):
    flattened_data = flatten(pixel_data)
    im = Image.new(mode='RGB', size=(len(pixel_data), len(pixel_data[0])))
    im.putdata(flattened_data)
    with open(path, 'wb') as f:
        im.save(f, format='JPEG')