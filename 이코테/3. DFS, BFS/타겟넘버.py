from collections import deque

def BFS(numbers, target):

  queue = deque()
  queue.append(0)

  for i in range(len(numbers)):
    temp = []
    for element in queue:
      temp.append(element + numbers[i])
      temp.append(element - numbers[i])
    queue = temp[:]

  return queue.count(target)

def solution(numbers, target):
    return BFS(numbers, target)