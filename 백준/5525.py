# N = int(input())
# M = int(input())
# S = input()

# pn = "IO" * N + "I"
# pnNum = len(pn)

# answer = 0
# for i in range(M-pnNum+1):
#     if S[i] == "I" and S[i:i+pnNum] == pn:
#         answer += 1

# print(answer)

N = int(input())
M = int(input())
S = input()

pn = "IO" * N + "I"
pnNum = len(pn)

cur = 0
answer = 0
count = 0
while cur < M -1:
    if S[cur:cur+3] == "IOI":
        cur += 2
        count += 1
        if count == N:
            answer += 1
            count -= 1
    else:
        cur += 1
        count = 0

print(answer)