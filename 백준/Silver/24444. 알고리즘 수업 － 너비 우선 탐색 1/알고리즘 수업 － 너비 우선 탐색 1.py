#https://www.acmicpc.net/problem/24444

import sys
from collections import deque

N,M,R = map(int,(sys.stdin.readline().split()))

graph=[[] for _ in range(N+1)]
for _ in range(M):
  a,b = map(int, sys.stdin.readline().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(N+1):
    graph[i].sort()


def bfs(graph, R, visited):
  queue = deque([R])
  visited[R] = 1
  count = 2

  while queue:
    R = queue.popleft()

    for i in graph[R]:
      if visited[i] == 0:
        queue.append(i)
        visited[i] = count
        count += 1  # n+1 번째 방문 정점

visited=[0]*(N+1)

bfs(graph,R,visited)

for i in visited[1::]:
    print(i)