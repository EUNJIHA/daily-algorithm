# # 8:50 - 9:10
# from collections import defaultdict

# def solution(id_list, report, k):
#     answer = []

#     finalReport = set(report)

#     # 신고당한 횟수 테이블 만들기
#     reportTable = defaultdict(int)
#     userReportTable = defaultdict(list)
#     for re in finalReport:
#         arr = re.split()
        
#         reportTable[arr[1]] += 1
#         userReportTable[arr[0]].append(arr[1])

#     # answer 구하기 
#     blockedUser = [key for key, value in reportTable.items() if value >= k]
#     for id in id_list:
#         answer.append(len(set(blockedUser) & set(userReportTable[id])))

#     return answer

def solution(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))