# from itertools import combinations 

# def solution(n):
#     answer = 0
#     if n % 2 == 0:
#         for i in range(0, n+1, 2): # FIXME: 반절만 계산해도 됨
#             answer += len(list(combinations(range(1, n+1), i)))
#             print(list(combinations(range(1, n+1), i)))
#     else:
#         for i in range(1, n+1, 2):
#             answer += len(list(combinations(range(1, n+1), i)))
#     return answer % 1000000007

# print(solution(4))

def solution(n):
    dp = [0 for i in range(60001)]
    
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000007 # 분배법칙. 이를 이용하지 않으면 효율성 테스트 fail
        
    return dp[n]