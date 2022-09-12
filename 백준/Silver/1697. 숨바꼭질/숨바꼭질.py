import sys
from collections import deque
#https://www.acmicpc.net/problem/1697

n,k = map(int, sys.stdin.readline().split())
max_input = (10 ** 5) *2

visited = [0] * (max_input+1)
q = deque([n])

while q:
    tmp = q.popleft()
    if tmp == k:
        break
    for x in (tmp-1, tmp+1, tmp*2):
        if 0<=x<=max_input and not visited[x]:
            q.append(x)
            visited[x] = visited[tmp]+1

print(visited[k])