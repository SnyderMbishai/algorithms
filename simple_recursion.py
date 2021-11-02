def print_num(num):
    if (num < 1):
        return
    else:
        print(num, end=" ")
        print_num(num-1)
        print(num, end=" ")
        return

num = 3
print_num(num)