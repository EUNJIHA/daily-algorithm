import math

def manhattan_distance(pt1, pt2):
    distance = 0
    for i in range(len(pt1)):
        distance += abs(pt1[i] - pt2[i])
    return distance


def solution(numbers, hand):
    answer = ''
    
    dict = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1, 1), 6: (1, 2), 7: (2, 0), 8: (2, 1), 9: (2, 2), 10: (3, 0), 11: (3, 1), 12: (3, 2)}

    curRight = 10
    curLeft = 12

    for number in numbers:
        if number == 0:
            number = 11
    
        if number in [1, 4, 7]:
            answer += "L"
            curLeft = number
        elif number in [3, 6, 9]:
            answer += "R"
            curRight = number
        else:
            # TODO: 거리 구하기
            # dict[number]
            # dict[curRight]
            # dict[curLeft]
            disRight = abs(dict[number][0] - dict[curRight][0]) + abs(dict[number][1] - dict[curRight][1])
            disLeft = abs(dict[number][0] - dict[curLeft][0]) + abs(dict[number][1] - dict[curLeft][1])
            # disRight = math.dist(dict[number], dict[curRight])
            # disLeft = math.dist(dict[number], dict[curLeft])
            # disLeft, disRight = 0, 0
            if disLeft == disRight:
                # answer += "R" if hand == "right" else "L"
                if hand == "right":
                    answer += "R"
                    curRight = number
                else:
                    answer += "L"
                    curLeft = number
            elif disLeft < disRight:
                answer += "L"
                curLeft = number
            else:
                answer += "R"
                curRight = number
            

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))