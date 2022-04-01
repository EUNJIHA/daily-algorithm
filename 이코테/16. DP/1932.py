# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
# print(arr)
# for i in range(1, n):
#     for j in range(i+1):
#         if j == 0:
#             arr[i][j] += arr[i-1][j]
#         elif j == i:
#             arr[i][j] += arr[i-1][j-1]
#         else:
#             arr[i][j] += max(arr[i-1][j-1], arr[i-1][j])

# print(max(arr[n-1]))

import sys
read = sys.stdin.readline

n = int(read())
cache = []

for i in range(n):
    floor = list(map(int, read().split()))
    cache = [max(a+c, b+c) for a, b, c in zip([0]+cache, cache+[0], floor)]
print(max(cache))