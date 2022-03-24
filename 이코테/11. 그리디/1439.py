def solution():
    S = input()
    tmp = S[0]
    tmpList = [S[0]]
    
    for i in S:
        if tmp == i:
            continue
        else:
            tmp = i
            tmpList.append(i)

    if len(tmpList) == 1:
        return 0
    else:
        return min(tmpList.count("1"), tmpList.count("0"))

print(solution())