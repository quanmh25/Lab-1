# Chuỗi ký tự đặc biệt (ANSI escape codes) 

import time


set_color = "\x1b[48;5;"
end = "\x1b[0m"

def draw(offset, length, color):
    line = " " * length
    output = ' ' * offset + set_color + str(color) + 'm' + line + end
    #offset: độ dài khoảng cách ban đầu
    #line: độ dài của khoảng màu
    print(output)

    print(f'{' ' * offset}{set_color}{color}m{line}{end}')        # chỉ biến hoặc biểu thức cần được đánh giá mới đặt vô ngoặc nhọn
    # offset, indent, position: Có thể dùng để ký hiệu. Ý chỉ việc thụt vào đầu dòng


if __name__ == '__main__':

    # print("\x1b[48;5;222m Hello World! \x1b[0m")
    print(' ' * 5 + set_color + str(222) + 'm' + " hello" + ' ' * 5 + end)
    # print(' ' * space, set_color, str(color), 'm', ' ' * length, end)        # Dấu phẩy sẽ không đúng, thay vào đó phải dùng dấu +

    n = int(input())
    for i in range(n):
        draw(10,15,222)


