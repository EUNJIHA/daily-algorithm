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