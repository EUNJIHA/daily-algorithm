# from itertools import permutations

# def calculate(elements, operates):  # operates == ('*', '-', '+')
#     # print("들어왔다: ", elements, operates)
#     all_elements = elements
#     result = 0
    
#     for operate in operates:
#         while len(all_elements) != 1:
#             for i, element in enumerate(all_elements):
#                 # print(i, operate, all_elements)

#                 if element == operate:
#                     a = all_elements[i-1]
#                     b = all_elements[i+1]
#                     # print(a, b)
#                     if operate == "*":
#                         all_elements.insert(
#                             i+2, a * b)
#                     elif operate == "-":
#                         all_elements.insert(
#                             i+2, a - b)
#                     elif operate == "+":
#                         all_elements.insert(
#                             i+2, a + b)

#                     # TODO: 빼줘야지
#                     # if len(all_elements) > 4:
#                     del all_elements[i-1]
#                     del all_elements[i-1]
#                     del all_elements[i-1]
#                     # print(all_elements)
#                     break
#             if operate not in all_elements:
#                 break
#     # print(all_elements)
#     result = all_elements[0]
#     return result


# def solution(expression):
#     answer = 0
#     # 연산자 뽑기
#     # operates = []
#     # elements = []
#     # last_operate_index = -1
#     # for index, value in enumerate(expression):
#     #     if value == "-" or value == "*" or value == "+":
#     #         operates.append(value)
            
#     #         elements.append(int(expression[last_operate_index + 1:index])) 
#     #         elements.append(value)

#     #         last_operate_index = index
#     #         # expression = expression[index+1:]
#     # elements.append(int(expression[last_operate_index + 1:]))

#     # operates = list(set(operates))
#     # operate_combi = list(permutations(operates, len(operates)))


#     operators = [x for x in ['+', '-', '*'] if x in expression]
#     operator_combi = list(permutations(operators, len(operators)))
#     # 계산해서 최댓값 뽑기
#     # print("elements입니다. ", elements)
#     candidates = [abs(calculate(elements[:], i)) for i in operator_combi]
#     # print("candidates ", candidates)
#     answer = max(candidates)
#     return answer


# print(solution("100-200*300-500+20"))

# TODO: 1번째 풀이
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)

print(solution("100-200*300-500+20"))


# TODO: 2번째 풀이
# import re
# from itertools import permutations

# def solution(expression):
#     #1
#     op = [x for x in ['*','+','-'] if x in expression]
#     op = [list(y) for y in permutations(op)]
#     ex = re.split(r'(\D)',expression)

#     #2
#     a = []
#     for operators in op:
#         _ex = ex[:]
#         for operator in operators:
#             while operator in _ex:
#                 tmp = _ex.index(operator)
#                 _ex[tmp-1] = str(eval(_ex[tmp-1]+_ex[tmp]+_ex[tmp+1]))
#                 _ex = _ex[:tmp]+_ex[tmp+2:]
#         a.append(_ex[-1])

#     #3
#     return max(abs(int(x)) for x in a)

# print(solution("100-200*300-500+20"))
