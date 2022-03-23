
def solution():
    N, K = map(int, input().split())

    nSet = set(input() for _ in range(N))
    kSet = set(input() for _ in range(K))

    answerList = list(nSet.intersection(kSet))

    print(len(answerList))
    for i in sorted(answerList):
        print(i)

solution()