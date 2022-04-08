# N = int(input())
# arr = list(map(int, input().split()))

# sortedArr = sorted(list(set(arr)))

# def binarySearch(arr, num):
#     answer = -1
#     # 정렬되어 있다고 가정
#     start, end = 0, len(arr)-1
#     # mid = len(arr) // 2

#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] == num:
#             return mid
#         elif arr[mid] < num:
#             start = mid + 1
#         elif arr[mid] > num:
#             end = mid - 1

#     return answer

# answer = []
# for num  in arr:
#     answer.append(str(binarySearch(sortedArr, num)))

# print(' '.join(answer))

n = input()
nums = list(map(int, input().split(" ")))

arr = sorted(set((nums)))
print(arr)
num_dict = {n: i for i, n in enumerate(arr)}

print(" ".join([str(num_dict[num]) for num in nums]))