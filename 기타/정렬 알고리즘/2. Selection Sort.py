def selectionSort(arr):
    # 제일 작은 index 뽑기
    for i in range(len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        
        tmp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex]= tmp

    return arr

print(selectionSort([4, 2, 6, 1, 2, 6 ,20, 0]))