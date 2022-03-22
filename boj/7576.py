# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]

# def solution(m, n):
#     answer = 0

#     # 익은 토마토 찾기
#     ripedTomatos = []
#     rottenTomatosCount = 0
#     for i in range(n):
#         for j in range(m):
#             if box[i][j] == 1:
#                 ripedTomatos.append((i, j))
#             elif box[i][j] == -1:
#                 rottenTomatosCount += 1

#     # 이미 다 익은 상태라면
#     if len(ripedTomatos) == m*n - rottenTomatosCount:
#         return 0
    
#     # 날짜 세기
#     while True:
#         # 처리 하기
#         newRipedTomatos = []
#         for tomoto in ripedTomatos:
#             for x, y in zip(dx, dy):
#                 xx = tomoto[0] + x
#                 yy = tomoto[1] + y
#                 if xx >= 0 and yy >= 0 and xx < n and yy < m and box[xx][yy] == 0:
#                     box[xx][yy] = 1
#                     newRipedTomatos.append((xx, yy))
#         answer += 1

#         # 익지 않는 경우가 존재하면
#         if len(newRipedTomatos) == 0:
#             return -1
        
#         # 이미 다 익은 상태라면
#         if len(ripedTomatos) + len(newRipedTomatos) == m*n - rottenTomatosCount:
#             return answer
        
#         ripedTomatos += newRipedTomatos



# M, N = map(int, input().split())
# box = [list(map(int, input().split())) for _ in range(N)]

# print(solution(M, N))

def solution(m, n):
    answer = 0
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    # 익은 토마토 찾기
    ripedTomatos = []
    
    rottenTomatosCount = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 1:
                ripedTomatos.append((i, j))
            elif box[i][j] == -1:
                rottenTomatosCount += 1

    ripedTomatosCount = len(ripedTomatos)
    # 이미 다 익은 상태라면
    if ripedTomatosCount + rottenTomatosCount == m*n:
        return 0

    # 날짜 세기
    while True:
        # 처리 하기
        newRipedTomatos = []
        for tomoto in ripedTomatos:
            for x, y in zip(dx, dy):
                xx = tomoto[0] + x
                yy = tomoto[1] + y
                if xx >= 0 and yy >= 0 and xx < n and yy < m and box[xx][yy] == 0:
                    box[xx][yy] = 1
                    newRipedTomatos.append((xx, yy))
                    ripedTomatosCount += 1
        answer += 1

        # 익지 않는 경우가 존재하면
        if len(newRipedTomatos) == 0:
            return -1
        
        # 이미 다 익은 상태라면
        if ripedTomatosCount + rottenTomatosCount == m*n:
            return answer
        
        ripedTomatos = newRipedTomatos


M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]

print(solution(M, N))