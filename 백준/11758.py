# https://whitesnake.uzoo.in/79
def solution(p1, p2, p3):
    # 일직선 0: 기울기 같은지 확인
    # slope1 = p2[1] - p1[1] / p2[0] - p1[0]
    # slope2 = p3[1] - p2[1] / p3[0] - p2[0]
    # if slope1 == slope2:
    #     return 0
    answer = p1[1]*(p2[0]-p3[0]) + p2[1]*(p3[0]-p1[0]) + p3[1]*(p1[0]-p2[0])
    if answer > 0:
        return -1
    elif answer == 0:
        return 0
    elif answer < 0:
        return 1


a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

print(solution((a, b), (c, d), (e, f)))