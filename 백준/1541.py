# import re
# expression = input()
# ex_list = re.split(r'(\+|-)', expression)

# e_list = []
# for value in ex_list:
#     if value.isdigit():
#         e_list.append(str(int(value)))
#     else:
#         e_list.append(value)

# # e_list = [str(int(e)) for e in e_list if e.isdigit()]
# # print(e_list)

# while len(e_list) != 1:
#     e_index = [i for i in range(len(e_list)) if '-' in e_list[i]]
#     if len(e_index) == 0:
#         print(eval(expression))
#         break
#     elif len(e_index) == 1:
#         print(eval("".join(e_list[:e_index[0]])) - eval("".join(e_list[e_index[0]+1:])))
#         break
#     else:
#         e_list = e_list[:e_index[0]+1] + [str(eval("".join(e_list[e_index[0]+1:e_index[1]])))] + e_list[e_index[1]:]

# FIXME: 
expression = input()

elist = expression.split('-')
for idx, value in enumerate(elist):
    if value.isdigit():
        elist[idx] = str(int(value))
print(elist)
# answer = ""

answer = []
for idx, value in enumerate(elist):
    # if idx != 0:
    #     answer += '-'
    answer.append(str(eval(value)))
print(eval("-".join(answer)))
# print(eval(answer))

# TODO: 이해하기10-
a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)