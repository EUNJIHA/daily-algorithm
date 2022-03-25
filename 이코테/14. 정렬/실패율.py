# 처음 코드
# 테스트 22 〉	통과 (24.17ms, 18.4MB)
from collections import Counter

def solution(N, stages):
    counter = Counter(stages)
    failureRates = [] # (번호, 비율)

    for i in range(1, N+1):
        temp = 0
        for key, value in counter.items():
            if key >= i:
                temp += value
        if temp == 0:
            failureRates.append((i, 0))
        else:
            failureRates.append((i, counter[i] / temp)) 
    
    failureRates.sort(key= lambda x: x[1], reverse=True)
    return [x[0] for x in failureRates]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

# 리팩토링 - successPlayersCount를 두고 빼주는 아이디어.
# 테스트 22 〉	통과 (12.03ms, 18.3MB)
from collections import Counter

def solution(N, stages):
    counter = Counter(stages)
    failureRates = [] # (번호, 비율)
    successPlayersCount = len(stages)
    for i in range(1, N+1):
        if successPlayersCount == 0:
            failureRates.append((i, 0))
        else:
            failureRates.append((i, counter[i] / successPlayersCount))
            successPlayersCount -= counter[i]
        
    return [x[0] for x in sorted(failureRates, key= lambda x: x[1], reverse=True)]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

