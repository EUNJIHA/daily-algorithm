from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)

    for ticket in tickets:
        routes[ticket[0]].append(ticket[1])
    
    for route in routes:
        routes[route].sort()
    
    stack = ["ICN"]
    reverseRoute = []

    while len(stack) > 0:
        top = stack[-1]

        if top in routes and len(routes[top]) > 0:
            stack.append(routes[top].pop(0))
        else:
            reverseRoute.append(stack.pop())

    return reverseRoute[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))