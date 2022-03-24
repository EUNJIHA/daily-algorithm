# FIXME: 시간초과
# def solution():
#     str = input()
#     explosion = input()
    
#     length = len(str)

#     while length != 0:
#         str = "".join(str.split(explosion))
#         newLength = len(str)
        
#         if str == "":
#             str = "FRULA"
#             break

#         if length != newLength:
#             length = newLength
#         else:
#             break

#     return str

# print(solution())

# FIXME: 메모리 초과
# def solution():
#     str = input()
#     explosion = input()
#     eLen = len(explosion)
#     first = explosion[0]

#     answer = ""

#     while True:

#         fIdx = str.find(first)
#         idx = str.find(explosion)

#         if fIdx == idx:
#             answer += str[:idx]
#             str = str[idx+eLen:]
#         else:
#             answer += str[:fIdx]
#             str = str[fIdx:idx] + str[idx+eLen:]
        
#         if str == "":
#             return answer

#         if answer == "":
#             return "FRULA"

# print(solution())

def solution():
    str = input()
    explosion = input()
    eLen = len(explosion)
    end = explosion[-1]

    stack = []
    for s in str:
        stack.append(s)
        if s == end and "".join(stack[-eLen:]) == explosion:
            for _ in range(eLen):
                stack.pop()
    if not stack:
        return "FRULA"
    return "".join(stack)
        
print(solution())