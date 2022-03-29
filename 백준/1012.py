from collections import defaultdict, deque

T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())

    # graph 만들고
    # graph = defaultdict(list)
    cabbages = []
    for i in range(K):
        a, b = map(int, input().split())
        cabbages.append((a, b))
        # graph[a] = b


    # 모두 False 일 때 까지 count 세기
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    count = 0

    while cabbages:
        queue.append(cabbages.pop())
        while queue:
            cur = queue.popleft()
            for i in range(4):
                x = cur[0] + dx[i]
                y = cur[1] + dy[i]
                if (x, y) in cabbages:
                    queue.append((x, y))
                    cabbages.remove((x, y)) 
        count += 1

    print(count)