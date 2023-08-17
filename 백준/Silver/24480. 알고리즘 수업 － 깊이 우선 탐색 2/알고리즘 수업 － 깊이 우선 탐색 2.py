import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n, m, r = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
ans = [0] * (n + 1)
count = 1

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(node):
    global count
    visited[node] = 1
    ans[node] = count
    graph[node].sort(reverse=True)
    for g in graph[node]:
        if visited[g] == 0:
            count += 1
            dfs(g)

dfs(r)

for a in ans[1:]:
    print(a)