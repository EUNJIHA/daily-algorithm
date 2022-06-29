def solution(n):
    answer = n + 1
    while answer <= 1000000:
        if str(bin(n)).count('1') == str(bin(answer)).count('1'):
            return answer
        answer += 1
        
    return answer