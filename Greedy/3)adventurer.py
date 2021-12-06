# 1번째 풀이
N = int(input())
NArray = []
tempNum = 0
resultNum = 0

arr = list(map(int,input().split()))
arr.sort()

for element in arr:
  tempNum += 1
  if element <= tempNum:
    resultNum += 1
    tempNum = 0

print(resultNum)