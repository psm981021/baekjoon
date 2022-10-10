import sys

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

sum = 0
prefix_sum = [0]
for i in A:
    sum += i
    prefix_sum.append(sum)

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    print(prefix_sum[end] - prefix_sum[start - 1])
