


#https://www.acmicpc.net/problem/2667



import sys



n = int(sys.stdin.readline().rstrip())

m,homelist=[],[]
apt=0
for _ in range(n):
    m.append(list(map(int,list(input()))))


def dfs(x,y):
    global n,home
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=n or m[ny][nx]==0:
            continue
        else:
            m[ny][nx]=0
            home+=1
            dfs(nx,ny)


for y in range(n):
    for x in range(n):
        if m[y][x]==1:
            m[y][x]=0
            home=1
            dfs(x,y)
            apt+=1
            homelist.append(home)

homelist.sort()
print(apt)
print(*homelist,sep='\n')
