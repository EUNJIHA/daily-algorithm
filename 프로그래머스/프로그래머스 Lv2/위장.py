# from collections import defaultdict
# from itertools import combinations

# def solution(clothes):
#     answer = 0

#     dic = defaultdict(int)
#     for cloth in clothes:
#         dic[cloth[1]] += 1
#     dicLength = len(dic)

#     dicList = list(dic.values())
#     for i in range(1, dicLength + 1):
#         arr = combinations(range(dicLength), i)
#         # print("list is", arr)
#         for l in arr:
#             tmp = 1
#             # print("l is", l)
#             for j in l:
#                 # print("j is", j)
#                 tmp *= dicList[j]
#             answer += tmp
#     return answer


from collections import defaultdict


def solution(clothes):
    answer = 1
    dic = defaultdict(int)

    for cloth in clothes:
        dic[cloth[1]] += 1
    
    for num in dic.values():
        answer *= num + 1
    
    answer -= 1

    return answer

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
print(solution(	[["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))