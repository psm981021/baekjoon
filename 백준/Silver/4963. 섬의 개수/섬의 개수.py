import sys
from collections import deque
w=1
h=1
dx=[-1,1,0,0,-1,-1,1,1]
dy=[0,0,-1,1,-1,1,-1,1]
def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        x, y= q.popleft()
        for i in range(8):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1 and visited[nx][ny]==0 :
                q.append((nx,ny))
                visited[nx][ny]=1


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0: break
    graph=[]
    visited=[[0 for _ in range(w)]for _ in range(h)]
    cnt=0
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1 and visited[i][j]==0:
                bfs(i,j)
                cnt+=1
    
    

    print(cnt)