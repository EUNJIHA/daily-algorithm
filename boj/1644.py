# FIXME: 시간초과
# def getPrimeByEratos(n):
#     a = [False,False] + [True]*(n-1)
#     primes=[]

#     for i in range(2,n+1):
#         if a[i]:
#             primes.append(i)
#             for j in range(2*i, n+1, i):
#                 a[j] = False
#     return primes

# def solution():
#     N = int(input())
#     answer = 0

#     arr = getPrimeByEratos(N)

#     arr.reverse()
#     for idx, value in enumerate(arr):
#         count = 0
#         for i in arr[idx:]:
#             count += i
#             if count == N:
#                 answer += 1
#             elif count < N:
#                 continue
#             elif count > N:
#                 break

#     return answer


# print(solution())

def getNum(n, m, data):
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

def getPrimeByEratos(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

def solution():
    N = int(input())
    answer = 0

    arr = getPrimeByEratos(N)

    # 투포인터 알고리즘으로 count 세기 -> O(n)???
    return getNum(len(arr), N, arr)
    # length = len(arr)
    # answer, num, start, end = 0, 0, 0, 0
    # while True:
    #     if num > N:
    #         num -= arr[start]
    #         if start < length - 1:
    #             start += 1

    #     elif num == N:
    #         num -= arr[start]
    #         if start < length - 1:
    #             start += 1
    #         answer += 1
        
    #     elif num < N:
    #         num += arr[end]
    #         if end < length - 1:
    #             end += 1

    #     if start == length - 1 and end == length - 1:
    #         if num == N:
    #             answer += 1
    #         break
    # return answer 


print(solution())

# 이게 진짜
def getNum(n, m, data):
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

def getPrimeByEratos(n):
    a = [False,False] + [True]*(n-1)
    primes=[]

    for i in range(2,n+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                a[j] = False
    return primes

def solution():
    N = int(input())
    answer = 0

    arr = getPrimeByEratos(N)

    # 투포인터 알고리즘으로 count 세기 -> O(n)???
    return getNum(len(arr), N, arr)

print(solution())