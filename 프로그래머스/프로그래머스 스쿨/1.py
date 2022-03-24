import datetime

def whatIsNextTime(stringTime):
    nextTime = datetime.datetime.strptime(stringTime, "%H:%M") + datetime.timedelta(minutes=10)
    return nextTime.strftime("%H:%M")

def solution(booked, unbooked):
    answer = []

    # 제일 빠른 시각 구하기
    nextTime = "00:00"

    while booked or unbooked:
        # 예약된 손님 있는지 살피기
        if booked and booked[0][0] <= nextTime:
            answer.append(booked[0][1])
            nextTime = whatIsNextTime(booked[0][0])
            del booked[0]
        elif unbooked and unbooked[0][0] <= nextTime:
            answer.append(unbooked[0][1])
            nextTime = whatIsNextTime(unbooked[0][0])
            del unbooked[0]
        else:
            # 둘 중 제일 처음 시간 구하기
            if booked and unbooked:
                if booked[0][0] < unbooked[0][0]:
                    answer.append(booked[0][1])
                    nextTime = whatIsNextTime(booked[0][0])
                    del booked[0]
                else:
                    answer.append(unbooked[0][1])
                    nextTime = whatIsNextTime(unbooked[0][0])
                    del unbooked[0]
            elif booked:
                    answer.append(booked[0][1])
                    nextTime = whatIsNextTime(booked[0][0])
                    del booked[0]
            elif unbooked:
                    answer.append(unbooked[0][1])
                    nextTime = whatIsNextTime(unbooked[0][0])
                    del unbooked[0]

    return answer

print(solution([["09:55", "hae"], ["10:05", "jee"]],
      [["10:04", "hee"], ["14:07", "eom"]]))
