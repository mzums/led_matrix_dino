import board
import displayio
import framebufferio
import rgbmatrix
import time
import random

displayio.release_displays()

matrix = rgbmatrix.RGBMatrix(
    width=64, height=32, bit_depth=1,
    rgb_pins=[board.D6, board.D5, board.D9, board.D11, board.D10, board.D12],
    addr_pins=[board.A5, board.A4, board.A3, board.A2],
    clock_pin=board.D13, latch_pin=board.D0, output_enable_pin=board.D1
)
display = framebufferio.FramebufferDisplay(matrix, auto_refresh=True)

bitmap = displayio.Bitmap(display.width, display.height, 2)
palette = displayio.Palette(2)
palette[0] = 0x000000  # Czarny
palette[1] = 0xFFFFFF  # Biały

tile_grid = displayio.TileGrid(bitmap, pixel_shader=palette)
group = displayio.Group()
group.append(tile_grid)
display.root_group = group

arr = [65]
arr2 = [100]

def clear_bitmap():
    for x in range(display.width):
        for y in range(0, 29):
            bitmap[x, y] = 0

def draw_ground():
    for x in range(display.width):
        for y in range(29, display.height):
            bitmap[x, y] = 1

def draw_cactus(x):
    for i in range(21, 29):
        bitmap[x+2, i] = 1
        bitmap[x+3, i] = 1
    
    bitmap[x, 23] = 1
    bitmap[x, 24] = 1
    bitmap[x, 25] = 1
    bitmap[x+1, 25] = 1
    
    bitmap[x+5, 23] = 1
    bitmap[x+5, 24] = 1
    bitmap[x+4, 24] = 1


def draw_bird(x):
    bitmap[x, 15] = 1;
    bitmap[x+1, 15] = 1
    bitmap[x+1, 14] = 1
    bitmap[x+2, 15] = 1
    bitmap[x+2, 16] = 1
    
    bitmap[x+3, 16] = 1
    bitmap[x+4, 16] = 1
    bitmap[x+5, 16] = 1
    bitmap[x+6, 16] = 1
    bitmap[x+7, 16] = 1
    bitmap[x+8, 16] = 1
    
    bitmap[x+3, 17] = 1
    bitmap[x+4, 17] = 1
    bitmap[x+5, 17] = 1
    bitmap[x+6, 17] = 1
    bitmap[x+7, 17] = 1

    bitmap[x+4, 15] = 1
    bitmap[x+5, 15] = 1
    bitmap[x+6, 15] = 1
    bitmap[x+7, 15] = 1
    bitmap[x+5, 14] = 1
    bitmap[x+6, 14] = 1
    bitmap[x+7, 14] = 1
    bitmap[x+6, 13] = 1


def draw_bird2(x):
    bitmap[x, 15] = 1;
    bitmap[x+1, 15] = 1
    bitmap[x+1, 14] = 1
    bitmap[x+2, 15] = 1
    bitmap[x+2, 16] = 1
    
    bitmap[x+3, 16] = 1
    bitmap[x+4, 16] = 1
    bitmap[x+5, 16] = 1
    bitmap[x+6, 16] = 1
    bitmap[x+7, 16] = 1
    bitmap[x+8, 16] = 1
    
    bitmap[x+3, 17] = 1
    bitmap[x+4, 17] = 1
    bitmap[x+5, 17] = 1
    bitmap[x+6, 17] = 1
    bitmap[x+7, 17] = 1

    bitmap[x+4, 18] = 1
    bitmap[x+5, 18] = 1
    bitmap[x+6, 18] = 1
    bitmap[x+7, 18] = 1
    bitmap[x+5, 19] = 1
    bitmap[x+6, 19] = 1
    bitmap[x+7, 19] = 1
    bitmap[x+6, 20] = 1
    


while True:
    clear_bitmap() # custom
    draw_ground()
    for (i, x) in enumerate(arr):
        draw_cactus(x)
        arr[i] -= 1
        if arr[i] < -5:
            arr.pop(i)

    for (i, x) in enumerate(arr2):
        if random.randint(0, 2) == 0:
            draw_bird(x)
        else:
            draw_bird2(x)
        arr2[i] -= 1
        if arr2[i] < -5:
            arr2.pop(i)

    if (random.randint(0, 35) == 10) and (len(arr) == 0 or arr[len(arr)-1] < 40):
        arr.append(65)

    if (random.randint(0, 35) == 10 and (len(arr) == 0 or arr[len(arr)-1] < 30)) and (len(arr2) == 0 or arr2[len(arr)-1] < 40):
        arr2.append(65)

    display.refresh()
    time.sleep(0.02)
