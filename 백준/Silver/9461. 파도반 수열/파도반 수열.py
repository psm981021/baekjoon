#https://www.acmicpc.net/problem/9461


import sys
T = int(input())
dp = [0]*110
dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2
for i in range(6,105):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(T):
    N = int(sys.stdin.readline())
    print(dp[N])


