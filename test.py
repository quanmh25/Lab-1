from time import sleep
from os import system

WHITE = "\033[47m"
BLACK = "\033[40m"
i = 0
frames = ["|", "\\", "-", "/"]

if __name__ == "__main__":
    for i in range(300):
        f = i%4
        i = i//15
        download = f"Hacking Pentagon: {i*5}%" + "[" + WHITE + " "*(i) + BLACK + " "*(20-i) + "]" + BLACK + " "
        print(frames[f] + "  " + download)
        sleep(0.05)
        print("\033[H")


        