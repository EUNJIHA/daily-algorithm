# T = int(input())
# for _ in range(T):
#     n = int(input())
#     answer = 0

#     # 1개만 쓸 때
#     answer += 1
#     if n % 2 == 0:
#         answer += 1
#     if n % 3 == 0:
#         answer += 1

#     # TODO: 2개만 쓸 때

#     # 1, 2
#     if n - 3 >= 0:
#         # 일단 1, 2 각 한 개씩은 있음
#         twoNum = (n-3) // 2


#     # 1, 3
#     if n - 4 >= 0:


#     # 2, 3
#     if n - 5 >= 0:


#     # TODO: 3개만 쓸 때

#     print(answer)

T = int(input())
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

for _ in range(T):
    n = int(input())
    answer = 0

    if n >=1 and n <= 3:
        print(dp[n])
        continue
    else:
        for i in range(4, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n])
        continue
