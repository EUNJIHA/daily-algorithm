# int(input())
# map(int, input().split())

# def solution():
#     N = int(input())
#     tops = list(map(int, input().split()))
#     tops.reverse()
#     answer = []

#     for idx, top in enumerate(tops):
#         isFound = False
#         for tIdx, t in enumerate(tops[idx+1:]):
#             if top < t:
#                 answer.append(str(N-1 - (idx + tIdx)))
#                 isFound = True
#                 break
#         if not isFound:
#             answer.append("0")
#     answer.reverse()
#     return " ".join(answer)

# print(solution())

# https://jjangsungwon.tistory.com/44 참고
def solution():
    N = int(input())
    tops = list(map(int, input().split()))
    stack = [] # [1, 6], [2, 9], ... [번째, 탑 높이]
    answer = []

    for idx, top in enumerate(tops):
        isFound = False
        while stack:
            cur = stack[-1]
            if cur[1] > top:
                answer.append(str(cur[0]))
                isFound = True
                break
            else:
                stack.pop()
        stack.append([idx+1, top])
        if not isFound:
            answer.append("0")

    return " ".join(answer)

print(solution())