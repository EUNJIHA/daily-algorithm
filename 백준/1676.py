N = int(input())
num = 1
for i in range(1, N+1):
    num *= i

for idx, value in enumerate(reversed(str(num))):
    if value != "0":
        print(idx)
        break