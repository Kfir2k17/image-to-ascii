import os, sys
from PIL import Image

txt = open("text.txt", "w")

COLORS = "MNHQ$OC?7>!:-;. "

im1 = Image.open("image.jpg")
im1 = im1.convert("L")

width, height = im1.size

im2 = Image.new("RGB", (width, height))

for y in range(height):
    for x in range(width):
        p = im1.getpixel((x, y))

        txt.write(COLORS[int(p // 16)])

        txt.write("  ")
    txt.write("\n")

txt.close()
