from collections import defaultdict
def calculate(arr1, arr2, operator):
    temp = []
    for i in arr1:
        for j in arr2:
            try:
                temp.append(int(eval(str(i) + operator + str(j))))
            except:
                pass

    return temp

def solution(N, number):
    answer = -1
    
    # DP 저장소
    DP = defaultdict(list)
    
    for i in range(1, 9):
        numbers = []
        
        # numbers 채우기
        numbers.append(int(str(N)*i))
        for j in range(1, i):
            numbers += calculate(DP[j], DP[i-j], "+")
            numbers += calculate(DP[j], DP[i-j], "-")
            numbers += calculate(DP[j], DP[i-j], "*")
            numbers += calculate(DP[j], DP[i-j], "//")
        
        numbers = list(set(numbers))
        
        if number in numbers:
            return i
        else:
            DP[i] = numbers
            
    return answer

print(solution(2, 11))