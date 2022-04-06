# from collections import defaultdict

# N = int(input())
# time = defaultdict(list)
# dp = defaultdict(int)

# last = 0
# for _ in range(N):
#     a, b = map(int, input().split())
#     time[b].append(a) # 거꾸로 저장
#     dp[b] = 0
#     last = b

# dp[0] = 0
# prev = 0
# prevIdx = 0

# for idx, values in sorted(time.items()):
#     if idx == 0:
#         dp[0] = len(time[0])
#         prev = dp[0]
#         continue

#     plusOne = False
#     for value in values:
#         if value == idx:
#             plusOne = True
#             continue
#         tmp = 0
#         if value >= prevIdx:
#             tmp = prev + 1

#         dp[idx] = max(prev, dp[value] + 1, tmp)

#     if plusOne:
#         dp[idx] += 1


#     prevIdx = idx
#     prev = dp[idx]

# print(dp[last])


n = int(input())
s = []
for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])
s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])
last = 0
cnt = 0
for i, j in s:
    if i >= last:
        cnt += 1
        last = j
print(cnt)