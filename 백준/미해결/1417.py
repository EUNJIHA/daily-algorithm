# FIXME: 분리집합 사용안하고 푼 풀이 -> 시간 초과
def solution():
    n, m = map(int, input().split())
    calculations = [list(map(int, input().split())) for _ in range(m)]

    setList = []

    for cal in calculations:
        if cal[0] == 0:
            # setList에 cal[1], cal[2] 갖고 있는 대상 있는지 확인
            a = {cal[1]}
            b = {cal[2]}
            done = 0
            for s in setList:
                if done == 2:
                    break
                if cal[1] in s:
                    a = s
                    setList.remove(a)
                    done += 1
                elif cal[1] in s:
                    b = s
                    setList.remove(b)
                    done += 1
            setList.append(a | b)
        
        elif cal[0] == 1:
            answer = ""
            if cal[1] == cal[2]:
                answer = "yes"
            else:
                for s in setList:
                    if cal[1] in s and cal[2] in s:
                        answer = "yes"
                        break
            if len(answer) == 0 :
                answer = "no"
            print(answer)

print(solution())