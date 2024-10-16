from math import *


red = "\x1b[48;5;196m"
green = "\x1b[48;5;28m"
reset_color = "\x1b[0m"

if __name__ == '__main__':

    # with open("sequence.txt") as file:
    #         a = [abs(float(file.readline())) for _ in range(250)]

    file = open("sequence.txt")
    a = []
    for i in range(250):
        a.append(abs(float(file.readline())))
    file.close()

    s1, s2 = sum(a[:125]), sum(a[125:])
    per_1 = round(s1 / (s1 + s2) * 100, 1)
    per_2 = round(s2 / (s1 + s2) * 100, 1) 

    print(red + ' ' * int(per_1)+ reset_color + " процентное соотношение:" + str(per_1) + '%')
    print(green + ' ' * int(per_2) + reset_color + " процентное соотношение:" + str(per_2) + '%')

