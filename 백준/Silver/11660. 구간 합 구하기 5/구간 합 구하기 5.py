#https://www.acmicpc.net/problem/11660

import sys


n,m=map(int,sys.stdin.readline().split())
S=[[0]*(n+1)]



for _ in range(n):
    S.append([0]+list(map(int, sys.stdin.readline().split())))

#부분합 오른쪽 밑으로 내려가면서
for i in range(1, n+1):
    for j in range(1, n):
        S[i][j+1] += S[i][j]

for j in range(1, n+1):
    for i in range(1, n):
        S[i+1][j] += S[i][j]


for _ in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    print(S[x2][y2] - S[x2][y1 - 1] - S[x1- 1][y2] + S[x1- 1][y1- 1])

