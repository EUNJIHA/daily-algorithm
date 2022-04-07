N = int(input())
time = list(map(int, input().split()))

answer = []
tmp = 0
for i in sorted(time):
    tmp += i
    answer.append(tmp)
print(sum(answer))
