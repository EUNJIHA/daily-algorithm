from collections import deque

def solution():
    T = int(input())

    for i in range(T):
        p = input()
        n = int(input())
        tmp = input()
        arr = deque()
        if n != 0:
            arr = deque(tmp[1:-1].split(','))
        answer = True
        
        count = 0
        for f in p:
            if f == "R":
                count += 1
            elif f == "D":
                if not arr:
                    answer = False
                    break
                elif count % 2 == 0:
                    arr.popleft()
                elif count % 2 == 1:
                    arr.pop()
        if not answer:
            print("error")
        else:
            if count % 2 == 0:
                print("["+",".join(arr)+"]")
            else:
                print("["+",".join(reversed(arr))+"]")

solution()