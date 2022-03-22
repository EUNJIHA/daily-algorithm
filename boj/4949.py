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


# ["So when I die (the [first] I will see in (heaven) is a score list).", "[ first in ] ( first out ).", "Half Moon tonight (At least it is better than no Moon at all]."]

    # smallStack = []
    # largeStack = []
    # answer = "yes"

    # for s in str:
    #     if s == "(":
    #         # if largeStack:
    #         #     answer = "no"
    #         #     break
    #         # else:
    #         smallStack.append(s)
    #     elif s == "[":
    #         # if smallStack:
    #         #     answer = "no"
    #         #     break
    #         # else:
    #         largeStack.append(s)
    #     elif s == ")":
    #         if largeStack:
    #             answer = "no"
    #             break
    #         if smallStack and smallStack[-1] == "(":
    #             smallStack.pop()
    #     elif s == "]":
    #         if smallStack:
    #             answer = "no"
    #             break
    #         if largeStack and largeStack[-1] == "[":
    #             largeStack.pop()
    # if smallStack or largeStack:
    #     answer = "no"
    # return answer