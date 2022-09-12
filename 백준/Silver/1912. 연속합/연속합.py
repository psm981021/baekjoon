#https://www.acmicpc.net/problem/1138
#Kadane’s Algorithm


import sys

n = int(sys.stdin.readline())
seq = list(map(int,sys.stdin.readline().split()))


big = min(seq)
for i in range(1,n):
	seq[i] = max(seq[i],seq[i]+seq[i-1])
print(max(seq))



