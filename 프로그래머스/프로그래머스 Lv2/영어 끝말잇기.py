def solution(n, words):
    answer = [0, 0]

    seenWords = []
    tail = words[0][0]

    for idx, word in enumerate(words):
        if tail == word[0] and word not in seenWords:
            tail = word[-1]
            seenWords.append(word)
            continue
        else: # TODO: 탈락자 생기면
            answer = [idx % n + 1, idx // n + 1]
            break

    return answer