from collections import deque

def findShortestNum(start, end):
    visited = [False] * 100001
    answer = 0

    queue = deque([start])
    visited[start] = True

    while queue:
        for _ in range(len(queue)):
            cur = queue.popleft()
            if cur == end:
                return answer
            
            if cur - 1 >= 0 and cur - 1 < 100001 and not visited[cur-1]:
                queue.append(cur - 1)
                visited[cur-1] = True
            if cur + 1 < 100001 and not visited[cur+1]:
                queue.append(cur + 1)
                visited[cur+1] = True
            if cur * 2 < 100001 and not visited[cur*2]:
                queue.append(cur * 2)
                visited[cur*2] = True
        answer += 1

    return answer


N, K = map(int, input().split())
print(findShortestNum(N, K))
