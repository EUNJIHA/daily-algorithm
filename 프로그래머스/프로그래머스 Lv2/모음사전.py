from itertools import product

def solution(word):

    arr = ["".join(x) for x in product(['', 'A', 'E', 'I', 'O', 'U'], repeat=5)]
    sortedArr = sorted(list(set(arr)))
    return sortedArr.index(word)

print(solution("AAAAE"))