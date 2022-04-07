N = int(input())
score = []
for _ in range(N):
    score.append(int(input()))

dp = [0] * (N+1)
if N == 1: 
    print(score[0])

elif N == 2:
    print(score[0] + score[1])
else:
    dp[0] = score[0]
    dp[1] = score[0] + score[1]
    dp[2] = max(score[0] + score[2], score[1] + score[2])
    for i in range(3, N):
        dp[i] = max(dp[i-3] + score[i-1] + score[i], dp[i-2] + score[i])

    print(dp[N-1])