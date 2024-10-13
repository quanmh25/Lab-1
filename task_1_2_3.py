
from math import *


white = "\x1b[48;5;255m"
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
    print(white + '  ' * 11 + reset_color)
    print(white + '  ' * 2 + reset_color + '  ' * 5 + white + '  ' * 4 + reset_color)
    print(white + '  ' * 2 + reset_color + '  ' + white + '  ' * 3 + reset_color + '  ' + white + '  ' * 4 + reset_color)
    print(white + '  ' * 2 + reset_color + '  ' + white + '  ' + reset_color + '  ' * 3 + white + '  ' * 4 + reset_color)
    print(white + '  ' * 2 + reset_color + '  ' + white + '  ' + reset_color + '  ' + white + '  ' * 6 + reset_color)
    print(white + '  ' * 2 + reset_color + '  ' + white + '  ' + reset_color + '  ' * 5 + white + '    ' + reset_color)
    print(white + '  ' * 11 + reset_color)



#Task 3:
def func():
    for x in range(10, 0, -1):
        print(' ' * (2 * x + 3) + set_red + '*' + reset_color)


if __name__ == '__main__':
    print("Task 1:")
    flag()

    print('\n' + "Task 2:")
    pattern()

    print('\n' + "Task 3:")
    func()





