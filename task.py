
from math import *

set_green = "\x1b[48;5;28m"                # "\u001b[42m"
set_red = "\x1b[48;5;196m"                 # "\u001b[41m"
reset_color = "\033[0m"                    # "\u001b[0m"


# Task 1:
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

# Task 2:
def pattern():
    for y in range(5):
        for x in range(5):
            if y == 0:
                print(' ' * 5 + set_color + ' ' * 5 + reset_color, end ='')
            else:
                print(' ' * 5 + set_color + ' ' * 1 + reset_color + ' ' * 5)



#Task 3:
def func():
    for x in range(10, 0, -1):
        print(' ' * (2 * x + 3) + set_red + '*' + reset_color)



if __name__ == '__main__':
    print("Task 1:")
    flag()
    print('\n' + "Task 3:")
    func()





