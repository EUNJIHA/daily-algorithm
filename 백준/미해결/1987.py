# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]

# def dfs(board, start, visited):
#     for i in range(4):
#         x = start[0] + dx[i]
#         y = start[1] + dy[i]
#         if x >= 0 and y >= 0 and x < R and y < C:
#             if visited[x][y] == False and board[x][y] not in candidates:
#                 candidates.append(board[x][y])
#                 visited[x][y] = True
#                 dfs(board, (x, y), visited)
                
#                 candidates.pop()
#                 visited[x][y] = False
#         else:
#             answer.append(len(candidates))


# def solution():
#     global R, C
#     R, C = map(int, input().split())
#     board = [list(input()) for _ in range(R)]
#     visited = [[False]*C for _ in range(R)]
#     visited[0][0] = True

#     global answer
#     answer = []
#     global candidates
#     candidates = [board[0][0]]

#     dfs(board, (0, 0), visited)
    
#     return max(answer)


# print(solution())

# FIXME: 시간초과
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

answer = 0

def dfs(start):
    global answer
    for i in range(4):
        x = start[0] + dx[i]
        y = start[1] + dy[i]
        # if x >= 0 and y >= 0 and x < R and y < C and board[x][y] not in candidates:
        if x >= 0 and y >= 0 and x < R and y < C and alphabets[board[x][y]] == 0:
            alphabets[board[x][y]] = 1
            # candidates.append(board[x][y])
            dfs((x, y))
            # candidates.remove(board[x][y]) # 이게 벡트래킹이라고? 
            alphabets[board[x][y]] = 0
        else:
            if answer < alphabets.count(1):
                answer = alphabets.count(1)


def solution():
    global R, C
    R, C = map(int, input().split())
    global board
    # board = [list(input()) for _ in range(R)]
    board = [list(map(lambda x: ord(x)-65, input())) for _ in range(R)] # 아스키 코드로 바꿔줌
    global alphabets
    alphabets = [0]*26 # 알파벳 26개만큼 배열설정 
    alphabets[board[0][0]] = 1


    # global candidates
    # candidates = [board[0][0]]

    dfs((0, 0))
    
    return answer

print(solution())