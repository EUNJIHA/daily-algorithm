# BFS 구현
# Breath-First Search 너비 우선 탐색

from collections import deque
queue = deque()

# 첫번째: 큐에 삽입하고 방문처리하기
# 두번째부터: 큐에 있는 것 하나 빼서 방문하지 않은 것 있으면, 🖐🏼모두🖐🏼 큐에 넣고 방문처리하기
def bfs(graph, vertex, visited):
    queue.append(vertex)
    visited[vertex] = True
    print(vertex, end=' ')

    while queue:
        for i in graph[queue.popleft()]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                print(i, end=' ')
# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
  [],
  [2, 3, 8],
  [1, 7],
  [1, 4, 5],
  [3, 5],
  [3, 4],
  [7],
  [2, 6, 8],
  [1, 7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
bfs(graph, 1, visited)