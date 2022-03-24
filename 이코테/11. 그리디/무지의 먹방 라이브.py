# FIXME: 정확성 실패
# def solution(food_times, k):
#     allCount = len(food_times)
#     remainedCount = allCount
#     nextIdx = 0

#     for _ in range(k):
#         if remainedCount == 0:
#             return -1

#         while food_times[nextIdx] == 0:
#             if nextIdx == allCount - 1:
#                 nextIdx = 0
#             else:
#                 nextIdx += 1
        
#         food_times[nextIdx] -= 1
#         if food_times[nextIdx] == 0:
#             remainedCount -= 1

#         if nextIdx == allCount - 1:
#             nextIdx = 0
#         else:
#             nextIdx += 1        


#     return 1 if nextIdx == allCount - 1 else nextIdx + 1

# FIXME: 효율성 실패 - 시간초과
# from collections import deque

# def solution(food_times, k):
#     answer = -1
#     foodList = deque([idx + 1, value] for idx, value in enumerate(food_times))
    
#     for _ in range(k):
#         if not foodList:
#             break
#         curFood = foodList.popleft()
#         eatenFood = [curFood[0], curFood[1] - 1]

#         if eatenFood[1] != 0:
#             foodList.append(eatenFood)

#     if foodList:
#         return foodList[0][0]
#     else:
#         return answer


# FIXME: 정확성 1개 미통과 & 효율성 테스트 실패 
# def solution(food_times, k):
#     answer = -1
#     # foodList = deque([idx + 1, value] for idx, value in enumerate(food_times))
#     foodList = [[idx + 1, value] for idx, value in enumerate(food_times)]


#     count = k
#     while count > 0:
#         minFood = sorted(foodList, key= lambda x: x[1])[0]

#         if count - minFood[1] * len(foodList) < 0:
#             break
#         else:
#             count -= minFood[1] * len(foodList)
#             foodList = [[x[0], x[1] - minFood[1]] for x in foodList if x[1] - minFood[1] != 0]

#     for _ in range(count):
#         if not foodList:
#             break
#         curFood = foodList.pop(0) # {2:5}

#         eatenFood = [curFood[0], curFood[1] - 1]

#         if eatenFood[1] != 0:
#             foodList.append(eatenFood)

#     if foodList:
#         return foodList[0][0]
#     else:
#         return answer



import heapq

def solution(food_times, k):
    # 못하는 경우 미리 제거
    if sum(food_times) <= k:
        return -1 

    count = 0

    queue = []
    
    for idx, value in enumerate(food_times):
        heapq.heappush(queue, ((value, idx+1))) # (시간, 번호) 그래야 시간 순으로 정렬되어 들어감

    previous = 0

    while len(queue) * (queue[0][0] - previous) + count <= k:
        food = heapq.heappop(queue)
        newCount = (food[0] - previous) * (len(queue) + 1)
        previous = food[0]
        count += newCount
        
    remainedFoods = sorted(queue, key= lambda x: x[1])
    return remainedFoods[(k - count) % len(remainedFoods)][1]

print(solution([3, 1, 2], 5))