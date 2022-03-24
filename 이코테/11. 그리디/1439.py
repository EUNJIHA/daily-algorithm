def solution():
    S = input()
    tmp = S[0]
    tmpList = [S[0]]
    
    for i in S:
        if tmp != i:
            tmp = i
            tmpList.append(i)

    if len(tmpList) == 1:
        return 0
    else:
        return min(tmpList.count("1"), tmpList.count("0"))

print(solution())


# change = 0
# prev = '?'
# string = input()
# for i in string:
#     if i != prev:
#         change += 1
#     prev = i
# print(change//2)

# 다르게
def solution():
    S = input()
    tmp = "X"
    tmpList = []
    zeroCount, oneCount = 0, 0
    for i in S:
        if tmp != i:
            if i == "0":
                zeroCount += 1
            elif i == "1":
                oneCount += 1
            tmp = i

    return min(zeroCount, oneCount)

print(solution())