#https://www.acmicpc.net/problem/1822

import sys

nA, nB = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

result = A - B

print(len(result))
if len(result) > 0:
    print(*sorted(result))