# words = []
# num = int(input())
# for i in range(num):
#     words.append(input())

# answer = 0
# for word in words:
#     count = 0
#     temp = ""
#     for w in word:
#         if temp != w:
#             count += 1
#             temp = w
#     if len(set(word)) == count:
#         answer += 1

# print(answer)

# 3
# happy
# new
# year

result = 0
for i in range(int(input())):
    word = input()
    print(word.find)
    print(sorted(word))
    print(sorted(word, key=word.find))
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)