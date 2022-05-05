# 11:58 - 
def solution(board, moves):
    answer = 0

    # board 빼기 쉽게 변형
    realBoard = [[] for _ in range(len(board))]
    for b in reversed(board):
        for idx, a in enumerate(b):
            if a == 0:
                continue
            realBoard[idx].append(a)
    # move 돌면서
    bucket = [101]
    for move in moves:
        idx = move - 1
        if not realBoard[idx]:
            continue
        curItem = realBoard[idx].pop()
        if bucket[-1] == curItem:
            bucket.pop()
            answer += 2
        else:
            bucket.append(curItem)

    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))