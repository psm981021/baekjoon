import sys
import math
from collections import deque
from itertools import combinations



#https://www.acmicpc.net/problem/11723

m = int(sys.stdin.readline().rstrip())
result = 0

for _ in range(m):
    tmp = str(sys.stdin.readline().rstrip())
    if len(list(tmp.split())) == 2 :
        tmp, num = tmp.split()
        num = int(num)

    if tmp == 'add':
        result |= (1<<num)
    elif tmp == 'remove':
        result &= ~(1<<num)
    elif tmp == 'check':
        if result & (1<<num) == 0:
            print(0)
        else:
            print(1)
    elif tmp == 'toggle':
        result ^= (1<<num)
    elif tmp == 'all':
        result = (1 << 21)-1
    elif tmp == 'empty':
        result = 0








