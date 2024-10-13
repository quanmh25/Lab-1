from math import *

red = "\x1b[48;5;196m"
green = "\x1b[48;5;28m"
reset_color = "\x1b[0m"

# Open the file and read the data
try:
    with open("sequence.txt") as file:
        a = [abs(float(file.readline())) for _ in range(250)]
except FileNotFoundError:
    print("The file 'sequence.txt' was not found.")
    exit()
except ValueError:
    print("There was an error reading numbers from the file.")
    exit()

# Calculate sums and percentages
s1, s2 = sum(a[:125]), sum(a[125:])
s = s1 + s2
if s == 0:
    print("The sum of the numbers is zero; cannot calculate percentages.")
else:
    per_1, per_2 = s1 / s, s2 / s 

    # Print colored blocks
    print(red + ' ' * int(per_1 * 100) + reset_color)
    print(green + ' ' * int(per_2 * 100) + reset_color)
