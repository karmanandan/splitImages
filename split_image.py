from PIL import Image
import numpy as np

def split_images(image_path, crop_dim):
  # Open the image
  image = Image.open(image_path)

  # Get the size of the image
  width, height = image.size

  # Calculate the number of tiles in each dimension
  x_tiles = width // crop_dim
  y_tiles = height // crop_dim

  # Iterate through each tile
  for x in range(x_tiles):
    for y in range(y_tiles):
        # Crop the tile from the image
        left = x * tile_size
        top = y * tile_size
        right = left + tile_size
        bottom = top + tile_size
        tile = image.crop((left, top, right, bottom))
        # Save the tile
        tile.save(f"image_{x}_{y}.jpg")
split_images("/content/sample_data/1200px-ESC_large_ISS022_ISS022-E-11387-edit_01.jpg",256)
