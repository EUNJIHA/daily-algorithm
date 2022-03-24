import sys

def solution():
    n = int(input())
    arr = []
    for _ in range(n):
        # arr.append(input())
        arr.append(sys.stdin.readline().strip())

    arr.sort()
    for i in range(1, n):
        if arr[i].startswith(arr[i-1]):
            return "NO"
    
    return "YES"

t = int(input())
for _ in range(t):
    print(solution())