word = input()

special = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for s in special:
    word = word.replace(s, "0")

print(len(word))
