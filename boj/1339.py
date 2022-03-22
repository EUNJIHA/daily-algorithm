# int(input())
# map(int, input().split())

from collections import defaultdict

def solution():
    N = int(input())
    words = [input() for _ in range(N)]
    dictionary = defaultdict(int) # {'A' : 100, 'B' : 1010, ... }
    
    # dictionary 만들기
    for word in words:
        for idx, value in enumerate(reversed(word)):
            dictionary[value] += 10 ** idx

    # dictionary 정렬 후, 9부터 차례대로 부여하고, 정답 계산
    num = 9
    answer = 0
    for item in sorted(dictionary.items(), key = lambda x: x[1], reverse=True):
        answer += item[1] * num

        num -= 1

    return answer

print(solution())