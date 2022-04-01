def insertionSort(arr):
    
    for i in range(1, len(arr)):
        tmp = arr[i]
        prevIndex = i-1
        while(prevIndex >= 0 and arr[prevIndex] > tmp):
            arr[prevIndex + 1] = arr[prevIndex]
            prevIndex -= 1
        arr[prevIndex + 1] = tmp

    return arr

print(insertionSort([4, 2, 6, 1, 2, 6 ,20, 0]))