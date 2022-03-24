n = int(input())
words = []
for i in range(n):
    words.append(input())

for w in sorted(set(words), key=lambda x: (len(x), x)):
    print(w)