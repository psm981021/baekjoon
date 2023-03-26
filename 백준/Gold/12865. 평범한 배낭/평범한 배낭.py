#https://www.acmicpc.net/problem/12865
n, k = map(int, input().split())

weights = []
values = []
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= weights[i-1]: # 배낭에 넣을 수 있는 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]] + values[i-1])
        else: # 배낭에 넣을 수 없는 경우
            dp[i][j] = dp[i-1][j]
            
print(dp[n][k])