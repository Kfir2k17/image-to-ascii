from PIL import Image, PSDraw
import os

txt = open("text.txt", "w")

COLORS = "MNHQ$OC?7>!:-;. "

im1 = Image.open("image.jpg")
im2 = Image.open("bb.png")

def convert_image_to_ascii(image):
    image = image.convert("L")
    width, height = image.size

    for y in range(height):
        for x in range(width):
            p = image.getpixel((x, y))

            txt.write(COLORS[int(p // 16)])

            txt.write("  ")
        txt.write("\n")

    txt.close()

def convert_image_into_ascii_image(image):
    image = image.convert("L")
    width, height = image.size

    ps_file = open("write.ps", "wb")
    ps = PSDraw.PSDraw(ps_file)
    ps.begin_document()

    ps.setfont("Space Mono", font_size)

    for y in range(height):
        for x in range(width):
            p = image.getpixel((x, y))



convert_image_to_ascii(im1)