def solution():
    N = list(map(int, input()))

    if sum(N[:len(N)//2]) == sum(N[len(N)//2:]):
        return "LUCKY"
    else:
        return "READY"

print(solution())