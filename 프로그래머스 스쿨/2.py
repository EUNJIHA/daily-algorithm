def solution(people, tshirts):
    answer = 0
    
    people.sort()
    tshirts.sort()
    
    for person in people:
        if person in tshirts:
            idx = tshirts.index(person)
            answer += 1
            tshirts = tshirts[idx+1:]
        else:
            if tshirts and tshirts[-1] < person:
                return answer
            for index, tshirt in enumerate(tshirts):
                if tshirt > person:
                    answer += 1
                    tshirts = tshirts[index+1:]
    return answer

print(solution([2, 3],	[1, 2, 3]))