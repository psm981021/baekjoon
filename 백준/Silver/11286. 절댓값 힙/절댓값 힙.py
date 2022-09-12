import sys
from heapq import heappush, heappop


#https://www.acmicpc.net/problem/11286

n = int(sys.stdin.readline().rstrip())
heap = []
for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    if num == 0:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
    else:
        heappush(heap,(abs(num),num))



