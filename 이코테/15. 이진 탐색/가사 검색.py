from bisect import bisect
from collections import defaultdict


def solution(words, queries):
    answer = []

    classifiedWords = defaultdict(list)
    for word in words:
        classifiedWords[len(word)].append(word)

    answer = [] # (query, 개수) # FIXME: (idx, query, 개수)
    for idx, query in enumerate(queries):
        # 이미 나왔던 검색키워드인 경우 다음 수행 안하도록 TODO: 여기 시간 많이 쓸 듯?
        # bisect(answer, )
        exist = [(query, x[1]) for x in answer if x[0] == query] # TODO: 여기 선형 시간을 쓴단 말이지? -> 이진탐색으로 바꿀 수 있나? -> 정렬해야 함.
        if exist:
            answer.append(exist[0])
            continue

        # query의 길이만큼에 해당하는 것 words에서 찾아서 돌리기
        flag = True if query[0] == "?" else False
        
        # ?? 없애기
        target = ""
        if flag:
            target = query[query.rindex("?")+1:] 
        else:
            target = query[:query.index("?")] 

        tmp = 0


        for word in classifiedWords[len(query)]:
            if flag:
                if word.endswith(target):
                    tmp += 1
            else:
                if word.startswith(target):
                    tmp += 1
        answer.append((query, tmp))

    # FIXME: 여기도 바꿔줘야 함
    return [x[1] for x in answer]

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"], ["fro??", "fro??", "????o", "fr???", "fro???", "pro?"]))