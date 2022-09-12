

#https://www.acmicpc.net/problem/1931

import sys
import itertools

class_time=[]
n = int(sys.stdin.readline().rstrip())
for i in range(n):
    class_time.append(list(map(int,sys.stdin.readline().split())))

class_time.sort()

class_time = sorted(class_time, key = lambda x : x[1])

cnt = 0
finish = 0
while(1):
    for _ in class_time:
        if cnt == 0 :
            finish = _[1]
            cnt+=1
        else:
            if _[0] >= finish:
                finish = _[1]
                cnt+=1
            else:
                pass
    break

print(cnt)

