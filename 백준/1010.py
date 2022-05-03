T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    denominator, numerator = 1, 1
    bTmp = b
    for _ in range(a):
        denominator *= bTmp
        bTmp -= 1
    
    for y in range(a, 0, -1):
        numerator *= y

    print(int(denominator/numerator))