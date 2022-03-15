from collections import deque

def solution(cacheSize, cities):
    answer = 0
    queue = deque()

    for city in cities:
        city = city.lower()
        if city in queue:
            queue.remove(city)
            queue.append(city)
            answer += 1
        else:
            if len(queue) < cacheSize:
                queue.append(city)
            elif queue:
                queue.popleft()
                queue.append(city)
            answer += 5

    return answer

print(solution(2,	["Jeju", "Pangyo", "NewYork", "newyork"]))