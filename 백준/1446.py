# import sys
# import heapq
# N, D = map(int, sys.stdin.readline().split())
# graph = [[] for _ in range(D+1)]

# for i in range(D):
#     graph[i].append((i+1, 1))

# for i in range(N):
#     start, end, length = map(int, sys.stdin.readline().split())
#     if end > D: continue # D 넘어가는건 제외
#     graph[start].append((end, length))

# INF = 987654321
# distance = [INF]*(D+1)
# distance[0] = 0

# q = []
# heapq.heappush(q, (0, 0))
# while q:
#     d, now = heapq.heappop(q)
#     if distance[now] < d: continue

#     for x in graph[now]:
#         cost = d + x[1]

#         if distance[x[0]] > cost:
#             distance[x[0]] = cost
#             heapq.heappush(q, (cost, x[0]))

# print(distance[D])

# TODO: 
# import sys

# N, D = map(int, sys.stdin.readline().split())
# graph = [list(map(int, input().split())) for _ in range(N)]
# dis = [i for i in range(D+1)]

# # 0 부터 고속도로의 길이까지 반복하여 확인
# for i in range(d+1):

#     # 지름길로 간 거리와 고속도로로 간 거리를 비교
#     print(dis[i])
#     print(dis[i-1] + 1)
#     dis[i] = min(dis[i], dis[i-1]+1)

#     # 지름길을 반복하여 최단 거리를 찾는다.
#     for s, e, shortcut in graph:
#         if i == s and e <= d and dis[i]+shortcut < dis[e]:
#             dis[e] = dis[i]+shortcut

# # 고속도로의 끝에 도착했을 때까지 걸린 거리를 출력
# print(dis[d])


import sys

N, D = map(int, sys.stdin.readline().split())
graph = []
for i in range(N):
    start, end, shortcut = map(int, input().split())
    if end <= D: graph.append((start, end, shortcut)) # 거리 넘어가는 건 제외
dis = [i for i in range(D+1)] # [0, 1, 2, 3, ... D]

for i in range(D+1):
    dis[i] = min(dis[i], dis[i-1] + 1)

    for start, end, shortcut in graph: # 지름길 돌면서 업데이트하기
        if start == i:
            dis[end] = min(dis[start] + shortcut, dis[end])

print(dis[D])