s = input()

zero = 0

# 연속된 숫자 세기
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        continue
    else:
        zero += 1

print(zero // 2)