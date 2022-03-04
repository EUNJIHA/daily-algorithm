# from curses.ascii import isdigit

# return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))


# def solution(s):
#     answer = []
#     changedList = []
#     # 문자열 s 처리
#     temp = []
#     tempStr = ""
#     for i in s:
#         if i == "}":
#             if tempStr:
#                 temp.append(tempStr)
#                 tempStr = ""
#             if temp:
#                 changedList.append(temp)
#             temp = []
#         if i == ",":
#             if tempStr:
#                 temp.append(tempStr)
#                 tempStr = ""
#         if isdigit(i):
#             tempStr += i
    
#     changedList.sort(key = lambda x: len(x))
#     for value in changedList:
#         # 차집합 후 남은 원소 append
#         answer += list(set(value) - set(answer))
#     return list(map(int, answer))
import re
from collections import Counter

def solution(s):
    counter = Counter(re.findall('\d+', s))
    print(dict(sorted(counter.items(), key=lambda item: item[1])))
    return [int(x) for x in dict(sorted(counter.items(), key=lambda item: item[1], reverse=True))]



print(solution("{{20,111},{111}}"))
# [111, 20]
