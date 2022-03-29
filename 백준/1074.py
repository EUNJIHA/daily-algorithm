import math

def recursion(size, x, y):
    global count
    # 4등분 중 어느 위치인지 파악
    if size == 1:
        point = math.pow(2, size - 1)
        if x < point:
            if y < point:
                # 0, 0
                count += 0
            else:
                # 0, 1
                count += 1
        else:
            if y < point:
                # 1, 0
                count += 2
            else:
                # 1, 1
                count += 3
        print(int(count))
        return
    else:
        point = math.pow(2, size - 1)
        if x < point:
            if y < point:
                # 0, 0
                count += point * point * 0
                recursion(size-1, x, y)
            else:
                # 0, 1
                count += point * point * 1
                recursion(size-1, x, y - point)
        else:
            if y < point:
                # 1, 0
                count += point * point * 2
                recursion(size-1, x - point, y)
            else:
                # 1, 1
                count += point * point * 3
                recursion(size-1, x - point, y - point)

N, r, c = map(int, input().split())

count = 0
recursion(N, r, c)