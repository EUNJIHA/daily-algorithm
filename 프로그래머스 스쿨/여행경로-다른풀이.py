from collections import defaultdict
def solution(tickets):
    r = defaultdict(list)
    for i,j in tickets:
        r[i].append(j)
    for i in r.keys():
        r[i].sort()

    s = ["ICN"]
    p = []
    while s:
        q = s[-1]
        if r[q] != []:
            s.append(r[q].pop(0))
        else:
            p.append(s.pop())
    return p[::-1]

print(solution([["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]))