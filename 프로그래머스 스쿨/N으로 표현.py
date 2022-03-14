# from collections import defaultdict
# def calculate(arr1, arr2, operator):
#     temp = []
#     for i in arr1:
#         for j in arr2:
#             try:
#                 temp.append(int(eval(str(i) + operator + str(j))))
#             except:
#                 pass

#     return temp

# def solution(N, number):
#     answer = -1

#     # DP 저장소
#     DP = defaultdict(list)

#     for i in range(1, 9):
#         numbers = []

#         # numbers 채우기
#         numbers.append(int(str(N)*i))
#         for j in range(1, i):
#             numbers += calculate(DP[j], DP[i-j], "+")
#             numbers += calculate(DP[j], DP[i-j], "-")
#             numbers += calculate(DP[j], DP[i-j], "*")
#             numbers += calculate(DP[j], DP[i-j], "//")

#         numbers = list(set(numbers))

#         if number in numbers:
#             return i
#         else:
#             DP[i] = numbers

#     return answer

# print(solution(2, 11))


def solution(N, number):
    # s = [set()] * 9 # 이렇게 하면 같은 주소를 갖는 set()들
    s = [set() for x in range(9)] # index 1~8까지 사용하기 위해

    # for i, x in enumerate(s):
    #     if i == 0:
    #         continue
    #     x.add(int(str(N)*i))
    # for i in range(1, 9):  # 1, 2, ... 8
    #     for j in range(1, i):  # i == 3이면, 1, 2, 3 | 1 - 2, 2 - 1

    #         for op1 in s[j]:
    #             for op2 in s[i-j]:
    #                 s[i].add(op1 + op2)
    #                 s[i].add(op1 - op2)
    #                 s[i].add(op1 * op2)
    #                 if op2 != 0:
    #                     s[i].add(op1 // op2)
    #     if number in s[i]:
    #         return i
    return -1
print(solution(2, 11))




# TODO: 이전 코드 
def solution(N, number):
    # s = [set()] * 9 # index 1~8까지 사용하기 위해
    s = [set() for x in range(9)]
    for i, x in enumerate(s):
        if i == 0:
            continue
        x.add(int(str(N)*i))
    for i in range(1, 9): # 1, 2, ... 8
        for j in range(1, i): # i == 3이면, 1, 2, 3 | 1 - 2, 2 - 1
             
             for op1 in s[j]:
                 for op2 in s[i-j]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)
        if number in s[i]:
            return i
    return -1