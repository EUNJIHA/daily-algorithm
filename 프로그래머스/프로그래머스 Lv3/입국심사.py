# def solution(n, times):
#     answer = 0
#     times.sort()
#     queue = [[(0, time)] for time in times]

#     if n <= len(queue):
#         return queue[n-1][1]


#     for time in times:

#         tmp = time
#         arr.append((0, time))

#     for a in arr:

#         while tmp <= 1000000000 and len(arr) < n:
#             arr.append((tmp, tmp+time))
#             tmp = tmp+time
#     print(arr)
#     return answer

# def solution(n, times):
#     answer = 0
#     arr = []
#     for time in times:
#         tmp = time
#         while tmp <= 1000000000: # 안돼
#             arr.append(tmp)
#             tmp += time
#     arr.sort()
#     print(arr)
#     return arr[n-1]

# def solution(n, times):
#     answer = 0

#     length = len(times)
#     tmp = sorted(times)
#     arr = tmp[:]


#     # if n <= length:
#     #     return arr[n-1]

#     while len(arr) < n:
#         next = 1000000000
#         nextIdx = -1
#         for i in range(length):
#             element = times[i] + tmp[i]
#             if next > element:
#                 next = element
#                 nextIdx = i

#         arr.append(next)
#         tmp[nextIdx] = next

#     return arr[n-1]

def binarySearch(left, right, times, n):
    cnt=0
    answer = -1
    while left <= right:
        mid = int((left+right)/2)
        cnt = 0
        for time in times:
            cnt += int(mid/time)

        if cnt >= n: 
            if answer == -1:
                answer = mid
            else:
                answer = min(answer,mid)
            right = mid-1
        elif cnt < n: left = mid+1
            
    return answer

def solution(n, times):
    times.sort()
    left = 0
    right = times[-1]*n
    answer = binarySearch(left, right, times, n)
    print(answer)
    return answer


print(solution(6, [7, 10]))
