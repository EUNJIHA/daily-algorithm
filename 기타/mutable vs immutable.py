s1 = [set()] * 3
s2 = [set() for x in range(3)]

if s1[1] is s1[2]:
    print("s1 같습니다.")
else:
    print("s1 다릅니다.")

if s2[1] is s2[2]:
    print("s2 같습니다.")
else:
    print("s2 다릅니다.")

print()

d1 = [dict()] * 3
d2 = [dict() for x in range(3)]

if d1[1] is d1[2]:
    print("d1 같습니다.")
else:
    print("d1 다릅니다.")

if d2[1] is d2[2]:
    print("d2 같습니다.")
else:
    print("d2 다릅니다.")

print()
s
t1 = [tuple()] * 3
t2 = [tuple() for x in range(3)]

if t1[1] is t1[2]:
    print("t1 같습니다.")
else:
    print("t1 다릅니다.")

if t2[1] is t2[2]:
    print("t2 같습니다.")
else:
    print("t2 다릅니다.")