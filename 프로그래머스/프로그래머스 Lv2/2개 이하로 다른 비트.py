# FIXME: 테스트케이스 10, 11 시간초과
# def solution(numbers):
#     answer = []

#     for number in numbers:
#         tmpNumber = number + 1
#         while True:
#             if bin(tmpNumber ^ number).count('1') <= 2: # 비트 다른 지점 2개 이하
#                 answer.append(tmpNumber)
#                 break
#             else:
#                 tmpNumber += 1

#     return answer

def solution(numbers):
    answer = []

    for number in numbers:
        bin_number = list('0' + bin(number)[2:])
        idx = ''.join(bin_number).rfind('0')
        bin_number[idx] = '1'
        
        if number % 2 == 1:
            bin_number[idx+1] = '0'
        
        answer.append(int(''.join(bin_number), 2))

    return answer

print(solution([2, 7]))