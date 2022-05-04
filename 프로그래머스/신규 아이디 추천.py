# 11:23 - 11:57
import re

def solution(new_id):
    answer = ''
    # 1단계
    answer = new_id.lower()

    # 2단계
    # answer = re.sub('~!@#$%^&*()=+[{]}:?,<>/', '', answer)
    answer = re.sub('[^a-z0-9._\-]+', '', answer)
    
    # 3단계
    answer = re.sub('[.]+', '.', answer)

    # 4단계
    if answer and answer[0] == ".":
        answer = answer[1:]

    if answer and answer[-1] == ".":
        answer = answer[:-1]

    # answer = re.sub('^[.]|[.]$', '', answer)

    # 5단계
    if answer == "":
        answer = "a"
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    if answer[-1] == ".":
        answer = answer[:-1]    
    
    # 7단계
    if len(answer) <= 2:
        answer += answer[-1]*(3 - len(answer))
    return answer

print(solution(	"=.="))