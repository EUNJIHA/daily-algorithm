def solution(str):
    stack = []
    answer = "yes"

    for s in str:
        if s == "(":
            stack.append(s)
        elif s == "[":
            stack.append(s)
        elif s == ")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                answer = "no"
                break
        elif s == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                answer = "no"
                break
    if stack:
        answer = "no"
    return answer

while True:
    string = input()
    if string == ".":
        break
    print(solution(string))