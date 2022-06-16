# # 28분
# import math
# def solution(n,a,b):
#     answer = 0
#     depth = int(math.log2(n))

#     a, b = (a, b) if a < b else (b, a)

#     mid = n // 2

#     for i in range(depth, 0, -1):

#         if a <= mid and b > mid:
#             answer = i
#             break

#         if a <= mid and b <= mid:
#             mid -= 2 ** (i-2)
#         elif a > mid and b > mid:
#             mid += 2 ** (i-2)

#     return answer


def solution(n,a,b):
    answer = 0
    while a != b:
        answer += 1
        a, b = (a+1)//2, (b+1)//2

    return answer


print(solution(8, 7, 8))