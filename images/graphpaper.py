'Generates graph paper with multiple coordinate axes'

from PIL import Image
import numpy as np

dims = (5000, 3000, 3)
cols_center = dims[1] // 2
grid_spacing = 20
x_axis_spacing = 1000

pixels = np.full(dims, 255,  dtype=np.uint8)

lc = 200
line_color = (lc, lc, lc)
axis_color = (0, 0, 0)

for row in range(0, dims[0], grid_spacing):
    pixels[row, :] = line_color
for col in range(0, dims[1], grid_spacing):
    pixels[:, col] = line_color
pixels[:, cols_center - 1 : cols_center + 1] = axis_color
for x_axis_row in range(x_axis_spacing // 2, dims[0], x_axis_spacing):
    pixels[x_axis_row - 1 : x_axis_row + 1] = axis_color

img = Image.fromarray(pixels)
img.save('graphpaper.png')
