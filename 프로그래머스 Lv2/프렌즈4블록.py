from collections import defaultdict

def selectCandidates(x,y):
    try:
        if b[x][y] == b[x+1][y] == b[x][y+1] == b[x+1][y+1] and b[x][y] >= 'A' and b[x][y] <= 'Z':
            return {(x, y), (x+1, y), (x, y+1), (x+1, y+1)}
        else:
            return {}
    except:
        return {}

def solution(m, n, board):
    answer = 0    

    global b
    b = []

    for j in range(n):
        temp = []
        for i in reversed(range(m)):
            temp.append(board[i][j])
        b.append(temp)

    while True:
        candidates = set()
        for i in range(n-1):
            for j in range(m-1):
                candidates.update(selectCandidates(i, j))

        if len(candidates) == 0:
            break
        else:
            dd = defaultdict(list)
            for c in sorted(list(candidates)):
                dd[c[0]].append(c[1])
            
            for d in dd:
                for i in range(len(dd[d])):
                    del b[d][dd[d][i] - i]

            answer += len(candidates)

    return answer

print(solution(3,2, ["AA", "AA", "AB"]))