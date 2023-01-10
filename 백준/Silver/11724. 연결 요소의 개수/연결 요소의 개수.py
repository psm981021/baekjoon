#https://www.acmicpc.net/problem/11724

import sys

n,m = map(int,sys.stdin.readline().split())

graph = [[0]for _ in range(n)]

visited = [0] * n


for i in range(m):
    a, b = map(int, input().split())
    graph[a-1].append(b)
    graph[b-1].append(a)

def dfs(node, visited, adj_list):
    visited[node-1] = 1
    for i in adj_list[node-1]:
        if not visited[i-1]:
            visited[i-1] = 1
            dfs(i, visited, adj_list)

cnt = 0

for i in range(n):
    if visited[i] == False:
        dfs(i, visited, graph)
        cnt += 1

print(cnt)