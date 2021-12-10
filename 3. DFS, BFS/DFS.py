# DFS 구현
# Depth-First Search 깊이 우선 탐색

# 첫번째: 스택에 삽입하고 방문처리하기
# 두번째부터: 스택에 있는 것 하나 빼서 방문하지 않은 것이 있으면, 스택에 넣고 방문처리하기
def dfs(graph, vertex, visited):
    visited[vertex] = True
    print(vertex, end=' ')
    for i in graph[vertex]:
        if visited[i] == False:
            dfs(graph, i, visited)

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
dfs(graph, 1, visited)