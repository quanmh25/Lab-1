
# Practical lesson on Sat 05.10.24
import time

SET_COLOR = "\x1b[48;5;"            # Thiết lập màu nền
END = "\x1b[0m"                     # Đặt lại màu sắc về mặc định
CLEAR = "\033[H"                    # Di chuyển con trỏ về vị trí bắt đầu trong terminal
# CLEAR = "\033[2J"                 # Dùng để xóa màn hình

def draw(space, size):
    set_green = "\x1b[48;5;28m"
    set_red = "\x1b[48;5;196m"
    reset_color = "\033[0m"
    print(set_green + ' ' * space + set_red + '*' * size + set_green + ' ' * space + reset_color)


def draw_line(offset=0, length=1, color=222):
    line = " " * length
    print(f"{' ' * offset}{SET_COLOR}{color}m{line}{END}")
    
def draw_romb():
    size = 15
    center = size // 2
    offset = size // 2

    step = 1
    length = 1

    # print(size, center, offset)

    colors = [222, 157, 48]

    loop_cnt = 0  # biến đếm số lần lặp
    max_loop = 5  # giới hạn số lần lặp

    while loop_cnt < max_loop:
        for color in colors:
            for line in range(size):
                draw_line(offset, length, color)

                if line < center:
                    offset -= step
                    length += step * 2
                else:
                    offset += step
                    length -= step * 2 

            print(f"\x1b[{size+2}A")
            print(f"\x1b[{offset}D")

            length = 1
            offset = size // 2

            time.sleep(1)        # time between loops

        loop_cnt += 1
        # if input() == 'q':   # Enter q to stop
            # break
# Hoặc bấm Ctrl + C để dừng ctrinh trên Terminal

if __name__ == "__main__":
    draw_romb()
    # for i in range(20):
    #     draw_line(length=20, color=47, offset=i)
    #     print(f"{CLEAR}")
    #     time.sleep(0.5)

    draw(5, 10)