import sys

N = int(sys.stdin.readline())
dp = [[0 for i in range(15)] for j in range(15)]


def function(n,k):
    if dp[n][k] != 0:
        return dp[n][k]
    if k == 1:
        dp[n][k] = 1
        return k
    if n == 0:
        dp[n][k] = k
        return k
    return function(n,k-1) + function(n-1,k)


for i in range(N):
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    print(function(n, k))
