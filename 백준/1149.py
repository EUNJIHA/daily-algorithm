# N = int(input())
# cost = []
# for _ in range(N):
#     cost.append(list(map(int, input().split())))

# dp = [0] * N
# dp[0] = min(cost[0])
# lastColor = cost[0].index(dp[0])

# for i in range(1, N):
#     minValue = 1001
#     for j in [0, 1, 2]:
#         if j == lastColor:
#             continue
#         if minValue > cost[i][j]:
#             minValue = cost[i][j]
#             lastColor = j
    

#     # possibleColor = [x for x in [0, 1, 2] if x != lastColor]
#     # nextCost = min(cost[i][possibleColor[0]], cost[i][possibleColor[1]])
#     dp[i] = dp[i-1] + minValue

# print(dp[N-1])

N = int(input())
cost = []
for _ in range(N):
    cost.append(list(map(int, input().split())))

dp = [[0, 0, 0] for _ in range(N)]
dp[0] = cost[0]

for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N-1]))
