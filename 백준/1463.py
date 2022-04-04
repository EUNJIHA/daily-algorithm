# X = int(input())
# answer = 0
# while X != 1:
#     if X % 3 == 0:
#         X /= 3
#     elif X % 2 == 0:
#         X /= 2
#     else:
#         X -= 1
#     answer += 1

# print(answer)


X = int(input())
dp = [0] * (X+1)
for i in range(2, X+1):
    dp[i] = dp[i-1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
print(dp[X])