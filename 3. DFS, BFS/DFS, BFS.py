# 첫번째: 스택에 넣고 방문처리하기
# 두번째부터: 스택에 있는 것 하나 빼서 방문하지 않은 것이 있으면, 스택에 넣고 방문처리하기
def dfs(graph, vertex, visited):
    visited[vertex] = True # 스택에 넣고 방문처리하기
    print(vertex, end=' ') # TODO
    for i in graph[vertex]: # 스택에 있는 것 하나 빼서
        if visited[i] == False: # 방문하지 않은 것이 있으면
            dfs(graph, i, visited) # (재귀)


from collections import deque
queue = deque()

# 첫번째: 큐에 넣고 방문처리하기
# 두번째부터: 큐에 있는 것 하나 빼서 방문하지 않은 것 있으면, 🖐🏼모두🖐🏼 큐에 넣고 방문처리하기
def bfs(graph, vertex, visited):
    queue.append(vertex) # 큐에 넣고
    visited[vertex] = True # 방문처리하기
    print(vertex, end=' ') # TODO

    while queue:
        for i in graph[queue.popleft()]: # 큐에 있는 것 하나 빼서 (🖐🏼모두🖐🏼)
            if visited[i] == False: # 방문하지 않은 것이 있으면,
                queue.append(i) # 큐에 넣고
                visited[i] = True # 방문처리하기
                print(i, end=' ') # TODO