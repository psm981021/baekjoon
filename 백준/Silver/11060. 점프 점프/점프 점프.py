#https://www.acmicpc.net/problem/11060

import sys

n = int(sys.stdin.readline().rstrip())
maze = list(map(int,sys.stdin.readline().split()))
cnt = [0 for i in range(n)]

cnt[0] = 1
for i in range(n):
    '''
    if maze[i] == 0 :
        if i+1 <= n-1:
            if cnt[i+1] == 0:
                cnt[i+1] = -1
    
    '''
    if cnt[i] == 0 and i != 0 :
        continue
    for j in range(1,maze[i]+1):
        if i+j <=n-1 :
            if cnt[i+j] != 0 and cnt[i] != -1:
                min(cnt[i+j],cnt[i] + 1 )
            else:
                cnt[i+j] =  cnt[i] + 1

if cnt[-1] == -1 :
    print(-1)
else:
    print(cnt[-1] - 1)

