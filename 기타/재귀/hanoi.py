def hanoi(n, _from, _to, _assist): # from aux to
    if n == 1:
        print(_from, "->", _to)
        return
    hanoi(n-1, _from, _assist, _to)
    print(_from, "->", _to)
    hanoi(n-1, _assist, _to, _from)

hanoi(3, 1, 3, 2)
# 1 -> 3
# 1 -> 2
# 3 -> 2
# 1 -> 3
# 2 -> 1
# 2 -> 3
# 1 -> 3