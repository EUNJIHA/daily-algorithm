
from itertools import combinations

def cityChickenDistance(candidate):
    dist = 0

    for h in house:
        minDist = []
        for c in candidate:
            dis = abs(h[0]-c[0]) + abs(h[1]-c[1])
            minDist.append(dis)
        dist += min(minDist)

    return dist

def solution(N, M):
    answer = -1

    markets = [] # markets = [(0, 1), (1, 2)]
    global house
    house = []

    for i in range(N):
        for j in range(N):
            if cities[i][j] == 2:
                markets.append((i, j))
            elif cities[i][j] == 1:
                house.append((i, j))
    
    candidates = list(combinations(markets, M))

    for candidate in candidates:
        cityDist = cityChickenDistance(candidate)
        if answer == -1 or answer > cityDist:
            answer = cityDist

    return answer

# 입력
N, M = map(int, input().split())
cities = [list(map(int, input().split())) for i in range(N)]

print(solution(N, M))