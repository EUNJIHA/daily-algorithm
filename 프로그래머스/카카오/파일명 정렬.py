# from curses.ascii import isdigit

# def solution(files):
#     answer = []
#     # 3갈래로 나눈 Array 만들기
#     candidates = []
#     for file in files:
#         next = False
#         firstIdx = 0
#         secondIdx = len(file)
#         numCount = 0
        
#         for idx, f in enumerate(file):
#             if next and not f.isdigit():
#                 secondIdx = idx
#                 break
            
#             if not next and f.isdigit():
#                 firstIdx = idx
#                 next = True
#                 continue

#         element = [file, file[:firstIdx].lower(), int(file[firstIdx:secondIdx]), file[secondIdx:]]
#         candidates.append(element)

#     # 차례대로 정렬하기
#     candidates.sort(key= lambda x: x[1])

#     finalIdx = -1
#     prev = ""
#     for idx, candidate in enumerate(candidates):
#         if prev == candidate[1]:
#             answer.pop()
#             finalIdx = idx - 1
#             break
#         else:
#             answer.append(candidate[0])
#             prev = candidate[1]
    
#     if finalIdx == -1:
#         return answer

#     candidates = sorted(candidates[finalIdx:], key= lambda x: x[2])

#     prev = ""
#     for candidate in candidates:
#         answer.append(candidate[0])

#     return answer

# def solution(files):
#     answer = []

#     # TODO: head, number, tail 나누기


#     # TODO: 정렬하기

    

#     return answer

import re
def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]
    print(temp)

    sort = sorted(temp, key = lambda x: (x[0].lower(), int(x[1])))
    
    return [''.join(s) for s in sort]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))
print(solution(["O00321", "O49qcGPHuRLR5FEfoO00321"]))