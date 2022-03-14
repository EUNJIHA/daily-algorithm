# https://programmers.co.kr/learn/courses/30/lessons/17676
from datetime import datetime, timedelta

def solution(lines):
    answer = 0
    boundaries = []

    # 경계값들(끝 시간, 시작 시간) 모두 저장해두기. -> 탐색 대상?
    # 끝 시간 기준으로 정렬되어 있음
    for line in lines:
        log = line.split()
        endTime = log[1]

        log[1]
        startTime = datetime.strptime(log[1], "%H:%M:%S.%f") - timedelta(seconds=float(log[2][:-1])) #FIXME: 
        boundaries.append([startTime.strftime("%H:%M:%S.%f"), endTime])
    
    boundaries.sort()
    for index, boundary in enumerate(boundaries):
        temp = 0
        # 최대 개수 구하기
        for b in boundaries[index:]:
            plusOne = datetime.strptime(boundary[0], "%H:%M:%S.%f") + timedelta(seconds=1)
            if b[0] <= plusOne.strftime("%H:%M:%S.%f") or boundary[0] <= b[1]:
                temp += 1
                continue
            else:
                break

        if temp > answer:
            answer = temp

    return answer

print(solution(	["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]))