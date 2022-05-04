def solution(s):
    dict = {0:	"zero",
            1:	"one",
            2:	"two",
            3:	"three",
            4:	"four",
            5:	"five",
            6:	"six",
            7:	"seven",
            8:	"eight",
            9:	"nine"}
    
    for idx, value in dict.items():
        while s.find(value) != -1:
            s = s.replace(value, str(idx))

    return int(s)

print(solution("one4seveneight"))
