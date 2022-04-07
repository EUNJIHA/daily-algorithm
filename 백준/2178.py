from collections import deque

# 10: 55
N, M = map(int, input().split())

answer = 0
miro = [list(map(int, input())) for _ in range(N)]

queue = deque()
queue.append((0, 0))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# visited = [[False] * M for _ in range(N)]

while queue:
    answer += 1
    if (N-1, M-1) in queue:
        break
    for _ in range(len(queue)):
        cur = queue.popleft()

        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if x >= 0 and y >= 0 and x < N and y < M and miro[x][y] == 1:
                queue.append((x, y))
                miro[x][y] = 0
                # visited[x][y] = True
print(answer)