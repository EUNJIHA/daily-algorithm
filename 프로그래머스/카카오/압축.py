# 3:40 - 
def solution(msg):
    answer = []
    dict = {'A': 1, 'B':  2, 'C':  3, 'D':  4, 'E':  5, 'F':  6, 'G':  7, 'H':  8, 'I':  9, 'J':  10, 'K':  11, 'L':  12, 'M':  13, 'N':  14, 'O':  15, 'P':  16, 'Q':  17, 'R':  18, 'S':  19, 'T':  20, 'U':  21, 'V':  22, 'W':  23, 'X':  24, 'Y':  25, 'Z': 26}
    
    message = msg
    lastNum = 26
    w = ""

    while message:
        flag = True
        # if len(message) == 1:
        #     answer.append(dict[message])
        #     break
        for i in range(1, len(message)+1):
            tmp = message[:i]
            if tmp in dict.keys():
                w = tmp
                continue
            else:
                flag = False
                answer.append(dict[w])
                message = message[len(w):]

                if message:
                    lastNum += 1
                    dict[w + message[0]] = lastNum
                break
        if flag:
            answer.append(dict[w])
            break
    return answer

# print(solution("KAKAO"))
print(solution("ABABABABABABABAB"))



    # while cur != len(msg) - 1:
    #     flag = True
    #     for i in range(cur + 1, len(msg)):
    #         if msg[cur:i+1] in dict.keys():
    #             continue
    #         else:
    #             flag = False
    #             # cur = i - 1
    #             if i == cur+1:
    #                 dict[msg[cur:i+1]] = lastNum + 1
    #                 lastNum += 1
    #             answer.append(dict[msg[cur:i]])

    #             cur = i
    #             break
    #     if flag:
    #         cur = len(msg) - 1
    # answer.append(dict[msg[cur]])