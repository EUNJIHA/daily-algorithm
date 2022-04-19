def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while(left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while(right > start and array[right] >= array[pivot]):
            right -= 1
        if(left > right): # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

# arr = [7, 6, 5, 8, 3, 2, 9, 4, 1]
arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)



# def quick_sort(array):
#     # 리스트가 하나 이하의 원소만을 담고 있다면 종료
#     if len(array) <= 1:
#         return array

#     pivot = array[0] # 피벗은 첫 번째 원소
#     tail = array[1:] # 피벗을 제외한 리스트

#     left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
#     right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

#     # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)

# print(quick_sort(array))


# 시간복잡도
# 최선 O(nlogn)
# 최악 O(n^2) -> 오름차순 정렬, 내림차순 정렬 되어 있을 때 피봇을 최솟값 또는 최댓값을 선택한 경우
# 최악 개선하는 방법 -> 중간 값으로 설정.