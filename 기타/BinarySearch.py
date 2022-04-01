def binarySearch(arr, k):
    arr.sort()

    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = (start + end) // 2

        if arr[mid] == k:
            return mid
        elif arr[mid] > k:
            end = mid - 1
        else:
            start = mid + 1

    return None

print(binarySearch([4, 2, 6, 1, 2, 5, 6 ,20, 0], 5))
