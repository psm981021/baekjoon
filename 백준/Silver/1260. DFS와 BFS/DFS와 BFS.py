#https://www.acmicpc.net/problem/1260


from collections import deque
from sys import stdin
input = stdin.readline

n, m, start = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n + 1)
visited_bfs = [False] * (n + 1)

for i in range(m):
    a, b = map(int, input().split()) 
    if graph[a] == 0:                 
        graph[a] = [b]                
    else:
        graph[a].append(b)
    if graph[b] == 0:
        graph[b] = [a]
    else:
        graph[b].append(a)

for i in range(1, n+1):
    if type(graph[i]) == 'int': 
        continue
    else:
        graph[i].sort()

def dfs(start):
    visited_dfs[start] = True
    print(start, end=' ')
    for i in graph[start]:
        if not visited_dfs[i]:
            dfs(i)

def bfs(start):
    visited_bfs[start] = True
    que = deque([start])

    while que:
        temp = que.popleft()
        print(temp, end=' ')
        for i in graph[temp]:
            if not visited_bfs[i]:
                que.append(i)
                visited_bfs[i] = True


dfs(start)
print()
bfs(start)
