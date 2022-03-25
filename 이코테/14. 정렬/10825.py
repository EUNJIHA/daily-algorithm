N = int(input())
students = []

for _ in range(N):
    name, a, b, c = input().split()
    students.append((name, int(a), int(b), int(c)))
students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for s in students:
    print(s[0])