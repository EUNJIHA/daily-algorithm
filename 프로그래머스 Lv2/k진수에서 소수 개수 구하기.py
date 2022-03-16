import math

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def converse_number(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]

def solution(n, k):
    answer = 0

    number = converse_number(n, k)
    candidates = number.split("0")

    for c in candidates:
        try:
            if c == "0":
                continue
            else:
                if is_prime_number(int(c)):
                    answer += 1
        except:
            continue

    return answer


print(solution(110011,	10))
