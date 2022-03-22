import math

def solution(x, y):
    k = y - x
    tmp = 2 * math.sqrt(k) - 1
    if tmp.is_integer():
        return int(tmp)
    else:
        return int(math.ceil(tmp))

T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(solution(a, b))