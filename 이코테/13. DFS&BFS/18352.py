# int(input())
# map(int, input().split())

# from collections import defaultdict


# def dfs(vertex, visited, count):
#     global answer 

#     visited[vertex] = True # 스택에 넣고 방문처리하기
    
#     if count == K:
#         answer.append(vertex)
#         return

#     # print(vertex, end=' ') # TODO
#     for i in graph[vertex]: # 스택에 있는 것 하나 빼서
#         if visited[i] == False: # 방문하지 않은 것이 있으면
#             count += 1
#             dfs(i, visited, count) # (재귀)
#             count -= 1

# def solution():
#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a].append(b)

#     print(graph)
#     if X not in graph.keys():
#         return -1

#     dfs(X, visited, 0)

#     return sorted(answer)

# N, M, K, X = map(int, input().split())
# graph = defaultdict(list)
# visited = [False] * (N+1)
# answer = []

# print(solution())


# from collections import defaultdict

# def bfs(start, end, visited):


# def solution():
#     for _ in range(M):
#         a, b = map(int, input().split())
#         graph[a].append(b)

#     print(graph)
#     if X not in graph.keys():
#         return -1

#     bfs(X, visited, 0)

#     return sorted(answer)

# N, M, K, X = map(int, input().split())
# graph = defaultdict(list)
# visited = [False] * (N+1)
# answer = []

# print(solution())

# TODO:
# from collections import deque

# N, M, K, X = map(int, input().split())
# graph = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# # 최단거리 구하기
# dis = [-1] * (N+1)
# dis[X] = 0
# queue = deque([X]) # 첫번째 원소 집어넣은 상태

# while queue:
#     cur = queue.popleft()

#     for i in graph[cur]: # cur에 연결되어 있는 도시
#         if dis[i] == -1:
#             dis[i] = dis[cur] + 1
#             queue.append(i)

# # candidates = []
# flag = False
# for idx, value in enumerate(dis):
#     if value == K:
#         print(idx)
#         flag = True
#         # candidates.append(idx)

# if flag == False:
#     print(-1)

# from collections import deque

# # 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]

# # 모든 도로 정보 입력 받기
# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)

# # 모든 도시에 대한 최단 거리 초기화
# distance = [-1] * (n + 1)
# distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# # 너비 우선 탐색(BFS) 수행
# q = deque([x])
# while q:
#     now = q.popleft()
#     # 현재 도시에서 이동할 수 있는 모든 도시를 확인
#     for next_node in graph[now]:
#         # 아직 방문하지 않은 도시라면
#         if distance[next_node] == -1:
#             # 최단 거리 갱신
#             distance[next_node] = distance[now] + 1
#             q.append(next_node)

# # 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
# check = False
# for i in range(1, n + 1):
#     if distance[i] == k:
#         print(i)
#         check = True

# # 만약 최단 거리가 K인 도시가 없다면, -1 출력
# if check == False:
#     print(-1)


import heapq
import sys
read = sys.stdin.readline


def solve():
    N, M, K, X = map(int, read().split())
    # 인접 리스트
    adj = [list() for _ in range(N+1)]
    for _ in range(M):
        f, t = map(int, read().split())
        adj[f].append(t)

    # 최단 거리 배열
    min_dists = [300002] * (N+1)

    # 우선순위 큐
    # (해당 노드까지의 최단거리, 노드번호) 튜플을 원소로 가짐
    q = []
    heapq.heappush(q, (0, X))
    min_dists[X] = 0

    ans = []

    # 남은 모든 노드들에 대하여
    while q:
        # 우선순위 큐 안에 있는 최단 거리 노드 선택
        dist, node = heapq.heappop(q)
        # 이미 처리된 노드라면 continue
        if min_dists[node] < dist:
            continue

        # 현재 노드까지의 거리가 K라면 정답 리스트에 저장 후 continue
        if min_dists[node] == K:
            ans.append(str(node))
            continue

        # 연결된 노드들의 최단거리 갱신 후 우선순위 큐에 추가
        for to in adj[node]:
            if min_dists[to] > dist + 1:
                min_dists[to] = dist + 1
                heapq.heappush(q, (dist+1, to))

    return '\n'.join(ans) if ans else -1


print(solve())