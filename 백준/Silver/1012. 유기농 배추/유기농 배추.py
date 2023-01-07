
#https://www.acmicpc.net/problem/2667



import sys
sys.setrecursionlimit(2500)
def dfs(x,y):
    global n,home,r,c
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=N or ny<0 or ny>=N  or m[ny][nx]== 0 :
            continue

        else:
            m[ny][nx]=0
            dfs(nx,ny)

n = int(sys.stdin.readline().rstrip())

for s in range(n):
    r,c,b = map(int,input().split())
    N = max(r,c)
    m = [[0 for i in range(N)] for i in range(N)]
    li = []
    for i in range(b):
        c,d = map(int,sys.stdin.readline().split())
        li.append([d,c])
        m[d][c] = 1


    home = 1
    apt = 0
    for x in range(N):
        for y in range(N):
            if m[y][x] == 1:
                m[y][x] = 0
                dfs(x, y)
                apt += 1
    print(apt)






