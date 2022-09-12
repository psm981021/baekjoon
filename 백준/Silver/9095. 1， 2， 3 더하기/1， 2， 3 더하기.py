from calendar import c
import sys
import itertools

n = int(sys.stdin.readline().rstrip())
number = [1,2,3]

for i in range(n):
    cnt = 0
    num = int(sys.stdin.readline().rstrip())
    for j in range(1,num+1):
        for _ in list(itertools.product(number,repeat=j)):
            if sum(_)==num:
                cnt+=1
    print(cnt)