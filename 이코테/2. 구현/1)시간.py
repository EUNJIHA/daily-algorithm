# 첫번째풀이
n = int(input())
result = (n+1)*60*60

if n < 3:
  result -= (n+1)*45*45
elif n < 13:
  result -= (n)*45*45
elif n < 23:
  result -= (n-1)*45*45
elif n == 23:
  result -= (n-2)*45*45

print(result)