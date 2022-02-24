import math

def distance(x1, y1, x2, y2):
    return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

def m_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def solution(places):
    answer = []
    flag = False
    coordinates = []
    for i in range(5):
        for j in range(5):
            coordinates.append((i, j))
    for place in places:
        for row_index, row in enumerate(place):
            for col_index, col in enumerate(row):
                if col == "P":
                    # TODO: col과 거리 2 이하인 것 중 P들 찾기
                    candidates = []  # (1, 2) # (row_index, col_index)
                    for i, j in coordinates:
                        if m_distance(i, j, row_index, col_index) <= 2:
                            if row_index == i and col_index == j:
                                continue
                            candidates.append((i, j))
                    for a, b in candidates:
                        if place[a][b] == "P":
                            dis = distance(a, b, row_index, col_index)
                            if dis == 1.0:
                                answer.append(0)
                                # 처음 for문으로 가도록 처리
                                flag = True
                                break
                            elif dis == 2.0:
                                # 가운데가 X 인지 확인
                                if place[(a + row_index) // 2][(b + col_index) // 2] != "X":
                                    answer.append(0)
                                    flag = True
                                    break
                            elif dis == math.sqrt(2):
                                # X로 잘 둘러쌓여 있는지 확인
                                if place[a][col_index] == "O" or place[row_index][b] == "O":
                                    answer.append(0)
                                    flag = True
                                    break
                if (flag):
                    break
            if (flag):
                flag = False
                break
        else:
            answer.append(1)
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
      "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))

# import math

# def distance(x1, y1, x2, y2):
#     return math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

# def m_distance(x1, y1, x2, y2):
#     return abs(x1 - x2) + abs(y1 - y2)

# def solution(places):
#     answer = []
#     flag = False
#     coordinates = []
#     for i in range(5):
#         for j in range(5):
#             coordinates.append((i, j))
#     for index, place in enumerate(places):
#         print(index, "번째 place: ", place)

#         for row_index, row in enumerate(place):
#             for col_index, col in enumerate(row):
#                 print(row_index, col_index, col)
#                 if col == "P":
#                     # TODO: col과 거리 2 이하인 것 중 P들 찾기
#                     candidates = []  # (1, 2) # (row_index, col_index)
#                     for i, j in coordinates:
#                         if m_distance(i, j, row_index, col_index) <= 2:
#                             if row_index == i and col_index == j:
#                                 continue
#                             candidates.append((i, j))
#                     print("candidates: ", candidates)
#                     for a, b in candidates:
#                         print("place[a][b]: ", place[a][b], "row_index, col_index: ", row_index, col_index)
#                         if place[a][b] == "P":
#                             dis = distance(a, b, row_index, col_index)
#                             print("dis: ", dis)
#                             if dis == 1.0:
#                                 answer.append(0)
#                                 # 처음 for문으로 가도록 처리
#                                 flag = True
#                                 break
#                             elif dis == 2.0:
#                                 # 가운데가 X 인지 확인
#                                 if place[(a + row_index) // 2][(b + col_index) // 2] != "X":
#                                     answer.append(0)
#                                     flag = True
#                                     break
#                             elif dis == math.sqrt(2):
#                                 # X로 잘 둘러쌓여 있는지 확인
#                                 if place[a][col_index] == "O" or place[row_index][b] == "O":
#                                     answer.append(0)
#                                     flag = True
#                                     break
#                 if (flag):
#                     print("첫번째 flag: ", flag)
#                     break
#             if (flag):
#                 flag = False
#                 print("두번째 flag: ", flag)
#                 break
#         else:
#             answer.append(1)
#     return answer


# print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP",
#       "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
