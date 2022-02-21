import collections
def solution(participant, completion):
    dict = collections.Counter(participant) - collections.Counter(completion)
    return list(dict.keys())[0]


# def solution(participant, completion):
# 	dict = collections.Counter(participant) - collections.Counter(completion)

#     print(dict[0])


print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))


from collections import Counter
def solution(participant, completion):
    answer = ''
    if len(set(participant)) == len(set(completion)):
        dict = collections.Counter(participant) - collections.Counter(completion)
        answer = list(dict.keys()[0])
    else:
        answer = list(set(participant) - set(completion))[0]
    return answer