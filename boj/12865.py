# knapsack 알고리즘
def solution(n, k, objects):
    dp = [[0] * (k+1) for i in range(n+1)]
    objs = [[0, 0]] + objects
    
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if j >= objs[i][0]:
                dp[i][j] = max(objs[i][1] + dp[i-1][j-objs[i][0]], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][k]

n, k = map(int, input().split())
objects = [list(map(int, input().split())) for i in range(n)]

print(solution(n, k, objects))

# print(solution(4, 7, [[6, 13], [4, 8], [3, 6], [5, 12]]))