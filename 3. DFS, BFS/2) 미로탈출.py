from collections import deque

n, m = map(int, input().split())
graph = []
result = 0

queue = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


for i in range(n):
    graph.append(list(map(int, input())))

# 첫번째: 큐에 삽입하고 방문처리하기
# 두번째부터: 큐에 있는 것 하나 빼서 방문하지 않은 것 있으면, 🖐🏼모두🖐🏼 큐에 넣고 방문처리하기
def bfs(x, y):
    queue.append((x, y))

    
    while queue:
        x, y = queue.popleft()
        for i in range(4): # 여기서는 탐색 대상이 상, 하, 좌, 우 였던 것임
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 이 문제의 result 구하는 방식은 거리를 모두 더해놓고 맨 마지막 대상을 빼는게 정답임
                # 큐에 넣기
                queue.append((nx, ny))
    return graph[n-1][m-1]

print(bfs(0, 0))


