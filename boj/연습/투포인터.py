def getNum(n, m, data): # n: 배열 길이, m: 원하는 숫자, data: 배열
    count = 0
    interval_sum = 0
    end = 0

    # start를 차례대로 증가시키며 반복
    for start in range(n):
        # end를 가능한 만큼 이동시키기
        while interval_sum < m and end < n:
            interval_sum += data[end]
            end += 1
        # 부분합이 m일 때 카운트 증가
        if interval_sum == m:
            count += 1
        interval_sum -= data[start]

    return count

print(getNum(5, 5, [1, 2, 3, 2, 5]))


# FIXME: 이건 반례 있음 - 배열 내의 모든 수를 더해도 합보다 작을 때
# def solution(length, arr, num):
#     count = 0
#     start, end = 0, 0
#     sumNum = arr[0]
    
#     while True:
#         if sumNum == num: 
#             count +=1

#         if sumNum < num and end < length - 1:
#             end += 1
#             sumNum += arr[end]
#         elif sumNum >= num and start < length - 1:
#             sumNum -= arr[start]
#             start += 1
        
#         if start == end == length - 1:
#             if sumNum == num:
#                 count += 1
#             break

#     return count

# print(solution(5, [1, 1, 1, 1, 1], 10))