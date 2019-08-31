'Generates graph paper with multiple coordinate axes'

from PIL import Image
import numpy as np

rows = 5000
cols = 3000
cols_center = cols // 2
grid_spacing = 20
x_axis_spacing = 1000

pixels = np.zeros((rows, cols, 3), dtype=np.uint8)
pixels[:, :] = (255, 255, 255)

lc = 200
line_color = (lc, lc, lc)
axis_color = (0, 0, 0)

for row in range(0, rows, grid_spacing):
    pixels[row, :] = line_color
for col in range(0, cols, grid_spacing):
    pixels[:, col] = line_color
pixels[:, cols_center - 1 : cols_center + 1] = axis_color
for x_axis_row in range(x_axis_spacing // 2, rows, x_axis_spacing):
    pixels[x_axis_row - 1 : x_axis_row + 1] = axis_color

img = Image.fromarray(pixels)
img.save('graphpaper.png')
