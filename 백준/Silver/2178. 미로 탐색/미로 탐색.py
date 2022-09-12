import sys
from collections import deque
#https://www.acmicpc.net/problem/2178

N,M = map(int, sys.stdin.readline().split())
array=[]
for i in range(N):
    inpt = list(map(int,input()))
    array.append(inpt)

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def DFS(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()
        #상하좌우로 이동
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #미로를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            #벽인 경우는 무시
            if array[nx][ny] == 0:
                continue

            if array[nx][ny] == 1:
                array[nx][ny] = array[x][y] + 1
                queue.append((nx,ny))

    return array[N-1][M-1]

print(DFS(0,0))