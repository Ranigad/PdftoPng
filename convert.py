from wand.image import Image
from wand.color import Color
import sys

if __name__ == "__main__":
    filename, page_number = sys.argv[-1], 0
    with Image(filename=filename, resolution=300) as img:
        for page in img.sequence:
            with Image(width=img.width, height=img.height, background=Color("white")) as bg:
                bg.composite(page, 0, 0)
                bg.save(filename=f"./png/image{page_number}.png")
                page_number += 1