def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]
                # tmp = arr[j-1]
                # arr[j-1] = arr[j]
                # arr[j] = tmp
    return arr

print(bubbleSort([4, 2, 6, 1, 2, 6 ,20, 0]))