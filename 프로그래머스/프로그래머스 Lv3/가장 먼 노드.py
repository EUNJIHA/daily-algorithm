from collections import deque

def bfs(v, visited, adj):
    count = 0
    q = deque([[v, count]])
    while q:
        value = q.popleft()
        v = value[0]
        count = value[1]
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in adj[v]:
                q.append([e, count])


def solution(n, edge):
    answer = 0
    
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)
    
    # edge로 graph 만들기
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # 모든 간선 개수 세기
    bfs(1, visited, graph)
    
    # answer
    answer = visited.count(max(visited))
    
    return answer