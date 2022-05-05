# # 11:11 - 
# from datetime import datetime
# import re

# def solution(m, musicinfos):
#     answerArr = [] # (diff, title)
#     # musicinfos 하나씩 돌면서 분석
#     for index, music in enumerate(musicinfos):
#         arr = music.split(",")
#         # 초 계산하기
#         firstTime = datetime.strptime(arr[0], "%H:%M")
#         secondTime = datetime.strptime(arr[1], "%H:%M")
#         diff = int((secondTime - firstTime).total_seconds()//60)
#         musicStr = ""

#         # 실제 재생 문자열 구하기
#         musicArr = []
#         length = len(arr[3])

#         for s in arr[3]:
#             if s == "#":
#                 musicArr.append(musicArr.pop() + "#")
#             else:
#                 musicArr.append(s)

#         # 여기 처리해야 함.
#         if diff <= length:
#             musicStr = "".join(musicArr[:diff])
#         else:
#             musicStr = "".join(musicArr*(diff // length)) + "".join(musicArr[:diff % length])

#         idxArr = [idx.start() for idx in re.finditer(m, musicStr)]

#         for idx in idxArr:
#             if len(musicStr) > idx + len(m) and musicStr[idx + len(m)] == "#":
#                 continue
#             else:
#                 answerArr.append((diff, arr[2], index))

#     # answer 찾기
#     if not answerArr:
#         return "(None)"
#     else:
#         sortedArr = sorted(answerArr, key=lambda x: (-x[0], x[2]))
#         return sortedArr[0][1]

# print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
# print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))


# 3:00 - 3:20
from datetime import datetime
import re


def solution(m, musicinfos):
    answer = ''
    noteDict = {'C#': '1', 'D#': '2', 'F#': '3', 'G#': '4', 'A#': '5'}
    candidates = []

    for idx, value in noteDict.items():
        m = re.sub(idx, value, m)

    for index, musicinfo in enumerate(musicinfos):
        arr = musicinfo.split(",")
        delta = datetime.strptime(arr[1], "%H:%M") - datetime.strptime(arr[0], "%H:%M")
        diff = int(delta.total_seconds() // 60)
        
        song = arr[3]
        for idx, value in noteDict.items():
            song = re.sub(idx, value, song)
        
        finalSong = song * (diff // len(song)) + song[:diff % len(song)] # song[:diff] if len(song) < diff else

        if m in finalSong:
            candidates.append((diff, index, arr[2]))

    answerArr = sorted(candidates, key=lambda x: (-x[0], x[1]))
    return answerArr[0][2] if answerArr else '(None)'

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))

print("C#asdkjC#asdklC#".replace("C#", "바뀜"))