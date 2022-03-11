# https://programmers.co.kr/learn/courses/30/lessons/17676
def solution(lines):
    answer = 0
    boundaries = []
    # TODO: 경계값들(끝 시간, 시작 시간) 모두 저장해두기. -> 탐색 대상인 줄 알았는데 아닌 듯.
    # 끝 시간 기준으로 정렬되어 있음
    for line in lines:
        boundaries.append(line[0])
        boundaries.append(line[0] - line[1]) #FIXME:
    
    boundaries.sort()
    for boundary in boundaries:
        temp = 0
        # TODO: 최대 개수 구하기
        for boundary <= 끝시간 or 시작시간 <= boundary +1: #FIXME:
            temp += 1

        if temp > answer:
            answer = temp

    return answer

print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))