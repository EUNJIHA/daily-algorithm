# import itertools

# def solution(relation):
#     answer = 0
#     length = len(relation[0])
#     length_list = [i for i in range(length)]
#     candidates = []
    
#     for num in length:
#         temp_tuple = itertools.combinations(length_list, num)
#         for t in temp_tuple: # (0), (1), ... (0, 1), (1, 2), ...
#             temp = []
#             minimality = True
#             for r in relation:
#                 for i in t:
#                     temp.append(r[i])
#             # 유일성 확인
#             if len(list(set(temp))) == len(temp):
#                 candidates.append(t)
#                 # 최소성 확인
#                 for candidate in candidates:
#                     if set(candidate) == set(candidate).intersection(set(t)):
#                         minimality = False
#                         break
#                 if minimality:
#                     answer += 1
        
#     return answer


from itertools import combinations


def solution(relation):
    answer = 0
    colNum = len(relation[0])

    answerArr = []
    idxArr = [x for x in range(colNum)]
    
    for i in range(1, colNum + 1):
        candidates = combinations(idxArr, i)
        for candidate in candidates: # (1, 2, 3)
            # 최소성 만족
            flag = False
            for a in answerArr:
                if len(candidate) == len(set(candidate) | set(a)):
                    flag = True
                    break
            if flag:
                continue

            # 유일성 만족
            tmp = []
            for rel in relation:
                element = tuple()
                for c in candidate:
                    element += (rel[c],)
                tmp.append(element)
                    
            if len(tmp) == len(set(tmp)):
                answerArr.append(candidate)
                answer += 1      
    # print(answerArr)
    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))