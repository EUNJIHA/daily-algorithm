N, M = map(int, input().split())
chess = [input() for _ in range(N)]

# TODO: 최소 개수 구하기
def minNum(chess):
    answer = 0
    # 시작이 W
    for i in range(8):
        start = 'W' if i % 2 == 0 else 'B'
        for j in range(8):
            tmp = 'WBWBWBWB' if start == 'W' else 'BWBWBWBW'
            if chess[i][j] != tmp[j]:
                answer += 1
    return min(answer, 64-answer)

# TODO: 모두 살피기
answer = 65

for i in range(N-7):
    for j in range(M-7):
        tmpChess = []
        for x in range(i, i+8):
            tmpChess.append(chess[x][j:j+8])
        answer = min(answer, minNum(tmpChess))
    
print(answer)

# def makeChess(i, j):

#     for x in range(i, i+8):
#         chess[x][j:j+8]

#     chess[i][j:j+8]
#     chess[i+1][j:j+8]