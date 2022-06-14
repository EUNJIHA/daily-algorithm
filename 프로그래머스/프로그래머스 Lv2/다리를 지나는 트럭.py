# from collections import deque


# def solution(bridge_length, weight, truck_weights):
#     answer = 0

#     bridge = deque()
#     bridge_time = deque()

#     waiting = deque(truck_weights[:])

#     while bridge or waiting:
#         answer += 1

#         # 이미 있는 트럭 시간 계산
#         finishNum = 0
#         for i, time in enumerate(list(bridge_time)):
#             if time == bridge_length:
#                 finishNum += 1
#             else:
#                 bridge_time[i] = time + 1
        
#         for _ in range(finishNum):
#             bridge.popleft()
#             bridge_time.popleft()
        
#         # 무게 계산해서 더 넣을 수 있으면 넣기
#         if waiting and sum(bridge) + waiting[0] <= weight:
#             bridge.append(waiting.popleft())
#             bridge_time.append(1)
        
#         # print(answer, bridge, bridge_time)

#     return answer

# print(solution(2,10,[7,4,5,6]))

# 다른 풀이
# 시간계산을 queue의 popleft 등으로 활용, while에는 queue가 있는지 여부 판단
def solution(bridge_length, weight, truck_weights):
    q=[0]*bridge_length
    sec=0
    while q:
        sec+=1
        q.pop(0)
        if truck_weights:
            if sum(q)+truck_weights[0]<=weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec

# print(solution(2,10,[7,4,5,6]))
print(solution(100,	100,	[10,10,10,10,10,10,10,10,10,10]))