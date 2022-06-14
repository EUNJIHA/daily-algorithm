while True:
    word = int(input())
    if word == 0:
        break
    word = str(word)
    mid = len(word) // 2
    if len(word) % 2 == 0 and word[:mid] == word[mid:][::-1]:
        print('yes')
    elif len(word) % 2 == 1 and word[:mid] == word[mid+1:][::-1]:
        print('yes')
    else:
        print('no')
    