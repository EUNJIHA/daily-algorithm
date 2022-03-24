from itertools import combinations
def solution(n, info):
    answer = []
    scoreList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    info.reverse()
    info_plus_one = [x + 1 for x in info]
    print(info, info_plus_one)
    candidates = []

    maxLionScore = 0

    for i in range(1, n+1):

        p = combinations(scoreList, i)

        for j in p:
            tempCount = 0
            tempScore = 0
            for k in j:
                tempCount += info_plus_one[k]
                tempScore += k
            # print(i, j, tempCount)
            if tempCount == n:
                apeachScore = sum([x for x in list(set(scoreList) - set(j)) if info[x] != 0])
                if apeachScore < tempScore and maxLionScore <= tempScore:
                    candidates.append((j, tempScore))
                    maxLionScore = tempScore
    
    # TODO: candidates 중 점수 같은 것이 있을 경우 처리
    # print(candidates)
    if candidates:
        candidate = candidates[-1][0] # (6, 8, 9)
        answer = [0]*11
        for i in candidate:
            answer[i] = info_plus_one[i]
        answer.reverse()
        return answer
    else:
        return [-1]


print(solution(10, [0,0,0,0,0,0,0,0,3,4,3]))

# (0, 3, 4, 5, 6, 7, 8, 9, 10)

# [4, 5, 4, 1, 1, 1, 1, 1, 1]