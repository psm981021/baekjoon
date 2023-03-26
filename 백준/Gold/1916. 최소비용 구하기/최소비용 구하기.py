#https://www.acmicpc.net/problem/1916
import heapq
import sys

# 입력값 받기
n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))

start_node, end_node = map(int, sys.stdin.readline().split())

# 다익스트라 알고리즘
INF = int(1e9)
distance = [INF] * (n+1)
distance[start_node] = 0

q = []
heapq.heappush(q, (0, start_node))

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for next_node, next_cost in graph[now]:
        cost = dist + next_cost
        if cost < distance[next_node]:
            distance[next_node] = cost
            heapq.heappush(q, (cost, next_node))

# 결과 출력
print(distance[end_node])