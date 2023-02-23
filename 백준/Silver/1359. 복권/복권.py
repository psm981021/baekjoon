#https://www.acmicpc.net/problem/1359

import sys
import math

n,m,k = map(int, sys.stdin.readline().split())

def combination(n, m):
    if n < m: return 0
    return math.factorial(n) / (math.factorial(n-m) * math.factorial(m))

answer = 0
for K in range(k,m+1):
    answer += (combination(m,K)*combination(n-m,m-K)/combination(n,m))

print(answer)