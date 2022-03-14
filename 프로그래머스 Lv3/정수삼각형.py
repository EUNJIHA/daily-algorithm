def solution(triangle):
    dp = triangle[:]

    for i in range(1, len(dp)):
        for j in range(i+1):
            if j == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j]
            elif i == j:
                dp[i][j] = dp[i-1][j-1] + dp[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + dp[i][j]

    return max(dp[len(dp)-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))