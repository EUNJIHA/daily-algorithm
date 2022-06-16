# 13분
def isRight(s):
    stack = []
    for e in s:
        # if e in ['(', '[', '{']:
        #     stack.append(e)
        if stack and ((e == ')' and stack[-1] == '(') or (e == ']' and stack[-1] == '[') or (e == '}' and stack[-1] == '{')):
            stack.pop()
        else:
            stack.append(e)
    
    return not stack

def solution(s):
    answer = 0

    for i in range(len(s)):
        if isRight(s[i:] + s[:i]):
            answer += 1

    return answer

print(solution("}}}"))