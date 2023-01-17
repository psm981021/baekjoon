#https://www.acmicpc.net/problem/2468

import sys
from collections import deque


dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
def bfs(x,y,i):
    q=deque()
    q.append([x,y])
    visited[x][y]=1

    while q:
        x,y = q.popleft()
        for j in range(4):
            nx=x+dx[j]
            ny=y+dy[j]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny]>i and visited[nx][ny]==0:
                q.append([nx,ny])
                visited[nx][ny]=1


n= int(sys.stdin.readline())

graph=[]
res=[]




maxr=0

for _ in range(n):
    a=list(map(int, input().split()))
    maxr=max(maxr,max(a))
    graph.append(a)

for i in range(0,maxr):
    visited=[[0]*n for _ in range(n)]
    cnt=0
    for j in range(n):
        for k in range(n):
            if graph[j][k]>i and visited[j][k]==0:
                bfs(j,k,i)
                cnt+=1
    res.append(cnt)

print(max(res))

