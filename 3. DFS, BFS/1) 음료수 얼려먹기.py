# 문제 해설
n, m = map(int, input().split())
graph = []
result = 0

for i in range(n):
  graph.append(list(map(int, input().split())))


def dfs(x, y):
  if x < 0 or y < 0 or x >= n or y >= m:
    return False
  # 0 인게 있으면 가능성 있는 거임
  if graph[x][y] == 0:
    graph[x][y] = 1
    # 상, 하, 좌, 우
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True
  return False


for i in range(n):
  for j in range(m):
      if dfs(i, j) == True:
        result += 1

print(result)
