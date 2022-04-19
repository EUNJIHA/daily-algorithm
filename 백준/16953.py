from collections import deque

A, B = map(int, input().split())

answer = 0
queue = deque([A])
minNum = B

while queue:
    if B in queue:
        answer += 1
        break
    elif minNum > B:
        answer = -1
        break
    for _ in range(len(queue)):
        cur = queue.popleft()
        a = cur * 2
        b = int(str(cur) + "1")
        queue.append(a)
        queue.append(b)

        minNum = min(min(queue), a, b)
    answer += 1
print(answer)
