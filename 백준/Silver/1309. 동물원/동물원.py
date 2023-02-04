#https://www.acmicpc.net/problem/1309

import sys
N = int(sys.stdin.readline())

# dp[0] = 1 dp[1] = 3 dp[2] = 7 dp[3] = 17를 통해 점화식을 구한다

dp = [1 for i in range(N+1)]
dp[1] = 3

for i in range(2,N+1):
    dp[i] = dp[i-1]*2 + dp[i-2]
    dp[i] = dp[i] % 9901
print(dp[-1])