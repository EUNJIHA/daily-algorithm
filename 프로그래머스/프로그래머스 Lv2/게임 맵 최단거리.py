from collections import deque

def solution(maps):
    answer = 0
    row, col = len(maps), len(maps[0])
    visited = [[0] * col for _ in range(row)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    queue = deque([(0,0)])
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()

        if x == row-1 and y == col-1: # 최종 경로 도착
            answer = visited[x][y]
            return answer

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if visited[nx][ny] == 0 and maps[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx,ny))
    return -1

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))