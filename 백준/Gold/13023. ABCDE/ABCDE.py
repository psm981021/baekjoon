#https://www.acmicpc.net/problem/13023

import sys
n,m = map(int,sys.stdin.readline().split())
graph =[[] for _ in range(n)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * n

def dfs(node,depth):
    if depth == 5 :
        print(1)
        exit()
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(neighbor,depth+1)
    visited[node] = False



for i in range(n):
    dfs(i,1)
print(0)