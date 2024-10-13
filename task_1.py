
from math import *

set_green = "\x1b[48;5;28m"
set_red = "\x1b[48;5;196m"
reset_color = "\033[0m"


def flag():
    length, width = 40, 20
    radius = 3
    
    center_x = length // 2
    center_y = width // 2

    for y in range(width):
        for x in range(length):
            d = sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
            if d <= radius:
                print(set_red + ' ', end = '')
            else:
                print(set_green + ' ', end = '')
        print(reset_color)


if __name__ == '__main__':
    flag()
