def solution(n, lost, reserve):
    answer = 0
    arr = [1] * (n+2)
    arr[0] = 0
    arr[-1] = 0

    for i in lost:
        arr[i] -= 1
    for i in reserve:
        arr[i] += 1

    for i in range(1, n):
        if arr[i] == 0:
            if arr[i-1] > 1:
                arr[i] = 1
                arr[i-1] -= 1
            elif arr[i+1] > 1:
                arr[i] = 1
                arr[i+1] -= 1

    answer = len([k for k in arr if k > 0])
    return answer


print(solution(5, [2, 4], [1, 3, 5]))
