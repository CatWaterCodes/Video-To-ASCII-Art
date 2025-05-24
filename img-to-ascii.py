import PIL.Image as Image
from PIL import ImageDraw
from PIL import ImageFont
from math import ceil

def image_to_ascii(image_path: str, pixels_per_char = 8, background = (255,255,255), foreground = (0,0,0), letter_size = 20) -> Image:
    """Turns an image into ASCII art. It takes five parameters:
            image_path: str
            pixel_per_char=8 !!MUST BE PAIR!!
            background=(255,255,255)
            foreground=(0,0,0)
            letter_size=20

            -> output: PIL.Image"""
    assert pixels_per_char%2==0, "pixels_per_char must be pair"
    image = Image.open(image_path)
    bw_image = black_and_white(image)
    grid = translate_image(bw_image, pixels_per_char)
    letter_grid = image_grid_to_letter_grid(grid)

    final_render = Image.new(size=((len(letter_grid)+7)*letter_size, len(letter_grid)*letter_size), mode="RGB", color=background)
    draw = ImageDraw.Draw(final_render)
    font = ImageFont.truetype(font="JetBrainsMono-Bold.ttf", size=letter_size)

    y = 0
    for line in letter_grid:
        draw.text(xy=(0, y), text="".join(line), font=font, fill=foreground)
        y += letter_size

    return final_render

def black_and_white(image: Image) -> Image:
    width, height = image.size
    
    if image.mode != "RGB":
        image = image.convert(mode="RGB")

    for w in range(width):
        for h in range(height):
            r, g, b = image.getpixel((w,h))
            avg = round(r+g+b/3)
            image.putpixel((w,h), (avg, avg, avg))

    return image

def translate_image(image: Image, pixels_per_char: int) -> list:
    grid = image_to_grid(image, pixels_per_char)

    for y in range(len(grid)):
        for x in range(len(grid[0])):

            grid[y][x] = image_to_grid(grid[y][x], pixels_per_char//2) #I told you it needed to be divisible by 2... it's not necessary but it give BY FAR better results

    return grid

def image_to_grid(image: Image, pixels_per_cell: int) -> list:
    width, height = image.size
    
    grid = [[Image.new(size=(pixels_per_cell, pixels_per_cell), 
                mode="RGB", 
                color= ((255,255,255))
            ) 
            for y in range(ceil(width/pixels_per_cell))
        ]   
        for x in range(ceil(height/pixels_per_cell))
    ]

    for h in range(height):
        for w in range(width):
            grid[h//pixels_per_cell][w//pixels_per_cell].putpixel((w%pixels_per_cell, h%pixels_per_cell), image.getpixel((w, h)))
    
    return grid

def image_grid_to_letter_grid(grid: list):
    letter_dict = {
        "0000": " ",
        "0001": ".",
        "0010": ".",
        "0011": "_",
        "0100": "'",
        "0101": "]",
        "0110": "/",
        "0111": "J",
        "1000": "'",
        "1001": "\\",
        "1010": "[",
        "1011": "L",
        "1100": '"',
        "1101": "?",
        "1110": "P",
        "1111": "#"
    }

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] = letter_dict[convert_grid_to_key(grid[y][x])]
        
    return grid

def convert_grid_to_key(grid: list) -> str:
    key = ""
    width, height = grid[0][0].size

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            s = 0
            tq = width*height

            for w in range(width):
                for h in range(height):
                    s += grid[x][y].getpixel((w,h))[0]
            
            avg = s/tq
            if avg > 180:
                key += "0"
            else: 
                key += "1"

    return key
