def solution(n, arr1, arr2):
    answer = []

    for a, b in zip(arr1, arr2):
        # result = (bin(a|b).format(n))[2:]
        result = bin(a|b)[2:].zfill(n)

        print(result)
        tmp = ""
        for r in result:
            if r == "1":
                tmp += "#"
            else:
                tmp += " "
            # tmp += '#' if r == '1' else tmp += ' '
        answer.append(tmp)


    return answer

# print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))