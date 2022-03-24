def solution(priorities, location):
    answer = 0
    tupleList = [(v, k) for v, k in enumerate(priorities)]

    while tupleList:
        temp = tupleList.pop(0)

        if len(tupleList) == 0:
            answer += 1
            break

        if temp[1] < max([y for (x, y) in tupleList]):
            tupleList.append(temp)
        else:
            answer += 1
            if temp[0] == location:
                 break

    return answer

# MARK: 2번째 풀이
# def solution(priorities, location):
#     answer = 0
#     tupleList = [(v, k) for v, k in enumerate(priorities)]
    
#     while tupleList:
#         temp = tupleList.pop(0)
        
#         if temp[1] < max([y for (x, y) in tupleList] + [0]):
#             tupleList.append(temp)
#         else:
#             answer += 1
#             if temp[0] == location:
#                  break
        
#     return answer

# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         print([cur[1] < q[1] for q in queue])
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer

print(solution([1],	0))