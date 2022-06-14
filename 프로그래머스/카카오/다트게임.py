import re


def solution(dartResult):
    answer = 0
    # bonusAndOption = re.split("[0-9]+", dartResult)
    score = re.split("([0-9][0-9]|[0-9])", dartResult)[1:]
    print(score)

    # S D T
    for a, b in zip(score[0::2], score[1::2]):
        # tmp = 0
        # if len(b) == 1:
        if b[0] == "S":
            answer += int(a) ** 1
        elif b[0] == "D":
            answer += int(a) ** 2
        elif b[0] == "T":
            answer += int(a) ** 3

        if len(b) == 2:
            if b[1] == "*":
                answer *= 2
            elif b[1] == "#":
                answer *= -1

    return answer

print(solution("1S2D*3T"))