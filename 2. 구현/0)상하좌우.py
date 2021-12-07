# 1번째 풀이
n = int(input())
route = list(map(str, input().split()))

result = (1, 1)
temp = (0, 0)

for i in range(0, n):
  if route[i] == 'L':
    temp = tuple(sum(elem) for elem in zip(result, (0, -1)))
  elif route[i] == 'R':
    temp = tuple(sum(elem) for elem in zip(result, (0, 1)))
  elif route[i] == 'U':
    temp = tuple(sum(elem) for elem in zip(result, (-1, 0)))
  elif route[i] == 'D':
    temp = tuple(sum(elem) for elem in zip(result, (1, 0)))
    
  if temp[0] <= 0 or temp[1] <=0 or temp[0] > n or temp[1] > n:
    result = result
  else:
    result = temp

print(result[0], result[1])