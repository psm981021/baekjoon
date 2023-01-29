import sys
from collections import deque


readl = sys.stdin.readline
M, N = map(int, readl().split())
a = [list(map(int, readl().split())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]

q = deque()
d = ((-1, 0), (1, 0), (0, -1), (0, 1))

for sr in range(N):
    for sc in range(M):
        if a[sr][sc] == 1:
            q.append((sr, sc))
            dist[sr][sc] = 0

while q:
    r, c = q.popleft()
    for dr, dc in d:
        nr, nc = r + dr, c + dc
        if not 0 <= nr < N: continue
        if not 0 <= nc < M: continue
        # if a[nr][nc] == -1 : continue
        if a[nr][nc] == 0 and dist[nr][nc] == -1:
            dist[nr][nc] = dist[r][c] + 1
            q.append((nr, nc))

ans = -1
for r in range(N):
    for c in range(M):
        if dist[r][c] > ans: ans = dist[r][c]

for r in range(N):
    for c in range(M):
        if dist[r][c] == -1 and a[r][c] == 0: ans = -1

print(ans)