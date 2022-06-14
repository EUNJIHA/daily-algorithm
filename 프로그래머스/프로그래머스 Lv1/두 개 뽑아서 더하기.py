from itertools import combinations

def solution(numbers):
    answer = []
    for a, b in combinations(range(len(numbers)), 2):
        answer.append(numbers[a] + numbers[b])
    return answer

print(solution([2,1,3,4,1]))