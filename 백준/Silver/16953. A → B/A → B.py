#https://www.acmicpc.net/problem/16953

import sys

a,b = map(int,sys.stdin.readline().split())
cnt = 1

while b!= a :
    cnt += 1
    flag = True
    if b % 2 == 0:
        b //= 2
        flag = False
    elif b % 10 == 1:
        b //= 10
        flag = False
    if flag or a > b:
        print(-1)
        break

else:
    print(cnt)
