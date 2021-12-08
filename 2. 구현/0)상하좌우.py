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

# 대표 풀이
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)