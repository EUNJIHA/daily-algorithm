def solution(tickets):
    ticketsNum = len(tickets)
    answer = []
    caseStack = []
    stack = []

    lastCity = "ICN"
    
    while len(stack) != ticketsNum and tickets:
        tempCase = []
        
        for index, ticket in enumerate(tickets):
          if ticket[0] == lastCity:
            tempCase.append((len(stack), ticket))

        if tempCase:
          tempCase.sort()

          nextCase = tempCase.pop(0)
          stack.append(nextCase[1])
          lastCity = nextCase[1][1]
          tickets.remove(nextCase[1])

          caseStack += tempCase

        else:
          nextCase = caseStack.pop()

          while len(stack) != nextCase[0]:
            tickets.append(stack.pop())

          stack.append(nextCase[1])
          lastCity = nextCase[1][1]
          tickets.remove(nextCase[1])

    answer = [x[0] for x in stack]
    answer.append(stack[-1][1])
    
    return answer