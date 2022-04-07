N, M = map(int, input().split())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

candidates = []

# 4 * 1
for i in range(N-3):
    for j in range(M):
        candidates.append(paper[i][j] + paper[i+1][j] + paper[i+2][j] + paper[i+3][j])
# 1 * 4
for i in range(N):
    for j in range(M-3):
        candidates.append(paper[i][j] + paper[i][j+1] + paper[i][j+2] + paper[i][j+3])

# 2 * 2
for i in range(N-1):
    for j in range(M-1):
        candidates.append(paper[i][j] + paper[i+1][j] + paper[i][j+1] + paper[i+1][j+1])

# TODO: 2 * 3 (총 3가지)

# 가로 길게 2 * 3
for i in range(N-1):
    for j in range(M-2):
        tmp = [0, paper[i][j], paper[i][j+1], paper[i][j+2], paper[i+1][j], paper[i+1][j+1], paper[i+1][j+2]]
        for a, b in [(1, 3), (4, 6), (1, 6), (3, 4), (4, 5), (5, 6), (1, 2), (2, 3)]:
            sumTmp = sum(tmp)
            sumTmp = sumTmp - tmp[a]
            sumTmp = sumTmp - tmp[b]
            candidates.append(sumTmp)

# 세로 길게 3 * 2
for i in range(N-2):
    for j in range(M-1):
        tmp = [0, paper[i][j+1], paper[i+1][j+1], paper[i+2][j+1], paper[i][j], paper[i+1][j], paper[i+2][j]]
        # tmp = [0, paper[i][j], paper[i][j+1], paper[i+1][j], paper[i+1][j+1], paper[i+2][j], paper[i+2][j+1]]
        for a, b in [(1, 3), (4, 6), (1, 6), (3, 4), (4, 5), (5, 6), (1, 2), (2, 3)]:
            sumTmp = sum(tmp)
            sumTmp -= tmp[a]
            sumTmp -= tmp[b]
            candidates.append(sumTmp)

print(max(candidates))