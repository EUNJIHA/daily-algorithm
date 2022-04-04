# 9:51
from cmath import inf
from collections import deque


def kebinBaconNum(i, j, graph):
    visited = [False] * (len(graph) + 1)
    queue = deque([i])
    answer = 0

    while queue:
        answer += 1
        for _ in range(len(queue)):
            for g in graph[queue.popleft()]:
                if g == j:
                    return answer
                elif visited[g] == False:
                    visited[g] = True
                    queue.append(g)

    return answer


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

kebinBaconNumGraph = [[0]*(N+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(i+1, N+1):
        kebinBaconNumGraph[i][j] = kebinBaconNum(i, j, graph)

answer = [float(inf)]
for i in range(1, N+1):
    tmp = 0
    for j in range(1, N+1):
        if i > j:
            tmp += kebinBaconNumGraph[j][i]
        elif i < j:
            tmp += kebinBaconNumGraph[i][j]
    answer.append(tmp)

print(answer.index(min(answer)))