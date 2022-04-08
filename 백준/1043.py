N, M = map(int, input().split())

warning = set(list(map(int, input().split()))[1:])

if len(warning) == 0:
    print(M)
else:
    answer = 0
    remain = []

    isNew = True

    tmpNum = len(warning)
    for _ in range(M):

        participant = list(map(int, input().split()))[1:]
        if len(set(warning) & set(participant)) > 0:
            warning |= set(participant)
        else:    
            remain.append(participant)
    if tmpNum == len(warning):
        isNew = False 

    while remain and isNew:
        tmpNum = len(remain)

        for r in remain:
            if len(set(warning) & set(r)) > 0:
                isNew = True
                warning |= set(r)
                remain.remove(r)
        
        if tmpNum == len(remain):
            isNew = False

    for p in remain:
        if len(set(warning) & set(p)) == 0:
            answer += 1

    print(answer)