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

# 해답 - 거의 똑같음.
# n의 개수만큼 원소를 받을 수 있도록 리스트 길이 제한 걸어둬야 했는데, 그럴 필요까진 없나보네.
# 파이썬 오름차순 정렬  .sort() | 내림차순 정렬 .sort(reverse=True)
# 공백 기준 여러 개 입력 받기: list(map(int, input().split()))
# TODO: 그리디 > 오름차순으로 정렬 후, 현재 원소 숫자와 전체 개수 비교
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
  count += 1
  if count >= i:
    result += 1
    count = 0

print(result)