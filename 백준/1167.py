# # 1:33
# # TODO: 일단 어떤 식으로 저장할 것인가

# from collections import deque


# V = int(input())
# graph = [[] for _ in range(V+1)]
# for _ in range(V):
#     infoList = list(map(int, input().split()))
#     vertex = infoList[0]
#     edges = infoList[1:-1]
#     for a, b in zip(edges[0::2], edges[1::2]):
#         graph[vertex].append((a, b))



# # FIXME: 여기 구하지 않아도 되는 부분 구하고 있는 듯 
# # print(graph)
# # [1, 2, 5]
# # candidates = []
# # for i in range(1, V+1):
# #     if len(graph[i]) == 1:
# #         candidates.append(i)

# answer = []

# for i in range(1, V+1):
#     visited = [False] * (V+1)
#     # 하나 삽입학기 
#     queue = deque([i])
#     visited[i] = True

#     answerList = [0]
    
#     while queue:
#         tmpList = []
#         for j in range(len(queue)): # 개수는 answerList에 있는 것과 같음
#             cur = answerList[j]
#             for a, b in graph[queue.popleft()]:
#                 if visited[a] == False:
#                     visited[a] = True
#                     # TODO: answerList를 기반으로 계산해서 tmpList에 추가하기
#                     tmpList.append(cur + b)
#                     queue.append(a)
#         # 여기 고치기
#         if tmpList:
#             answerList = tmpList
    
#     answer += answerList
#     # print("answerList: ", answerList)

# print(max(answer))

# TODO: 시간초과나서 다른 풀이 참고
from collections import deque

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    infoList = list(map(int, input().split()))
    vertex = infoList[0]
    edges = infoList[1:-1]
    for a, b in zip(edges[0::2], edges[1::2]):
        graph[vertex].append((a, b))

def bfs(start):
    distance = [-1] * (V+1)
    queue = deque([start])
    distance[start] = 0
    distanceAndEdge = [0, 0]

    while queue:
        cur = queue.popleft()
        for a, b in graph[cur]:
            if distance[a] == -1:
                distance[a] = distance[cur] + b
                queue.append(a)
                if distanceAndEdge[0] < distance[a]:
                    distanceAndEdge = [distance[a], a]

    return distanceAndEdge

dis, node = bfs(1)
dis, node = bfs(node)
print(dis)
