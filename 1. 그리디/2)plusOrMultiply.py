# 1번째 풀이 (오답)
S = str(input())
left, right = 0, 0
result = 0

left = int(S[0])

for i in range(0, len(S)-1):
  right = int(S[i+1])
  if (left == 0 or right == 0):
    result = left + right
  else:
    result = left * right
  left = result

print(result)

# 2번째 풀이 (정답)
S = str(input())
left, right = 0, 0
result = 0

left = int(S[0])

for i in range(0, len(S)-1):
  right = int(S[i+1])
  if (left <= 1 or right <= 1):
    result = left + right
  else:
    result = left * right
  left = result

print(result)

# 예시 답안
data = input

result = int(data[0])

for i in range(1, len(data)):
  num = int(data[1])
  if num <= 1 or result <= 1:
    result += num
  else:
    result *= num

print(result)