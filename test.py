import time
import os

SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "[033[H"

WHITE = '\u001b[47m'
GREEN = '\u001b[42m'
BLUE = '\u001b[44m'
RED = '\u001b[41m'
END = '\u001b[0m'

def draw_line(offset=0, length=1, color=222):
    line = " " * length
    print(f"{' ' * offset}{SET_COLOR}{color}m{line}{END}")

def draw_graph():
    for x in range(15,-2,-1):
        if x == 15:
            print("    Y")
        elif 0 < x < 15:
            print(f'{x/2}{" " + BLUE + "  "}{END + "." *2*(x-1)}{RED + "  "}{END + "." * 2*(18-x)}' )
        elif x == 0:
            print(f'{"    " + BLUE + "  " * 20}{END + " X"}')
        else:
            print(f'{"     0 1 2 3 4 5 6 7 8 9 ..........."}')
    print()

def draw_circle():
    loop = 5
    for i in range (8):
        if i == 0:
            continue
        if  0 < i < 4:
            s1 = f'{" " * 2*(4-i)}{RED + " " *4*i}{END + " " *4*(4-i)}{RED + " " *4*i}{END + " " *2*(4-i)}'
            print(s1*loop)
        else:
            s2 = f'{" " * 2*(i-4)}{RED + " " *4*(8-i)}{END + " " *4*(i-4)}{RED + " " *4*(8-i)}{END + " " *2*(i-4)}'
            print(s2*loop)
    print()    
    
def draw_flag():
    for i in range(14):
        if i < 5:
            print(f'{WHITE}{"   " * 5}{BLUE}{"  " * 5}{WHITE}{"   " * 10}{END}')
        elif i < 9:
            print(f'{BLUE}{"     " * 11}{END}')
        else:
            print(f'{WHITE}{"   " * 5}{BLUE}{"  " * 5}{WHITE}{"   " * 10}{END}')
    print()

def filter_number():
    file = open('sequence.txt', 'r')
    list = []
    number = file.readline()
    count = 0
    count_all = 0
    while number != "":
        count_all += 1
        if (5 <= float(number) <= 10) or (-10 <= float(number) <= -5):
            list.append(float(number))
            count += 1
        number = file.readline()
    percent = (count/count_all) * 100
    
    print("List: ", end="")
    print(list)
    
    print(f'{GREEN}{"  "}{END}{" От 5 до 10 и От -10 до -5| кол-во: "}{count}{" | процентное соотношение: "}{round(percent , 1)}{" %"}')
    print(f'{RED}{"  "}{END}{" остальные | кол-во: "}{count_all}{" | процентное соотношение: "}{round(100-percent , 1)}{" %"}')
        
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    frames = [draw_flag, draw_circle, draw_graph, filter_number]
    for i in range(5):
        for j in range(len(frames)):
            clear_console()
            frames[j]()
            time.sleep(2)