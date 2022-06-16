# 문제: https://programmers.co.kr/learn/courses/30/lessons/43162

# 나의 풀이
def DFS(start, computers, visited, n):
    visited[start] = True
    for i in range(n):
        if start != i and computers[start][i] == 1 and visited[i] == False:
            DFS(i, computers, visited, n)
            
def solution(n, computers):
    visited = [False] * n
    count = 0
    
    while False in visited:
        # 가장 첫번째 False 인덱스
        DFS(visited.index(False), computers, visited, n)
        count += 1
    return count