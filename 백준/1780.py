N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))
answer = [0, 0, 0]

def solution(i, j, num):
    element = paper[i][j]

    if num == 1:
        answer[element+1] += 1
        return
    
    same = True
    for row in range(i, i + num):
        for col in range(j, j + num):
            if element != paper[row][col]:
                same = False
                break
        if not same:
            break
    
    if not same:
        for a in range(i, i+(num//3)*3, num//3):
            for b in range(j, j+(num//3)*3, num//3):
                solution(a, b, num//3)
    else:
        answer[element+1] += 1

solution(0, 0, N)
for i in range(3):
    print(answer[i])