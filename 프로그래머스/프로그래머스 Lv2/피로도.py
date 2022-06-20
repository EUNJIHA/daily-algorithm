from itertools import permutations


def solution(k, dungeons):
    answer = -1

    dungeons = [element for element in dungeons if element[0] <= k]
    # 모두 탐색 해보자 > 최대 8이니까. 8! == 40,320
    cases = permutations(dungeons, len(dungeons))

    for case in cases:
        tmpAnswer = 0
        tmpK = k
        for c in case:
            if c[0] <= tmpK:
                tmpK -= c[1]
                tmpAnswer += 1
        if answer < tmpAnswer:
            answer = tmpAnswer
        
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))