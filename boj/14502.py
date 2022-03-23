# int(input())
# map(int, input().split())

from collections import deque
from copy import deepcopy
from itertools import combinations

def bfs(laboratory, tuple, virus): # ((0, 1), (2, 1), (2, 3))

    for i in range(3):
        laboratory[tuple[i][0]][tuple[i][1]] = 1

    queue = deque(virus) # [(0, 1), (2, 1), (2, 3)]

    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    newVirusCount = 0

    while queue:
        cur = queue.pop()
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if x >= 0 and y >= 0 and x < N and y < M and laboratory[x][y] == 0:
                laboratory[x][y] = 2
                queue.append((x, y))
                newVirusCount += 1

    return newVirusCount

def solution():
    n, m = map(int, input().split())
    global N, M
    N = n
    M = m

    laboratory = [list(map(int, input().split())) for _ in range(N)]

    blank = []
    blankCount = 0
    virus = []
    for i in range(N):
        for j in range(M):
            if laboratory[i][j] == 0:
                blank.append((i, j))
                blankCount += 1
            elif laboratory[i][j] == 2:
                virus.append((i, j))

    candidates = []
    for c in list(combinations(blank, 3)):
        candidates.append(blankCount -  bfs(deepcopy(laboratory), c, virus) - 3)
        
    return max(candidates)

print(solution())