#https://www.acmicpc.net/problem/2251

from collections import deque
a,b,c = map(int, input().split())

def check(x, y):
    if not visited[x][y]:
        visited[x][y] = True
        q.append((x, y))

#조합의 수를 계산해서 반복문 돌ㄹ려고 했는데 실패함
def bfs():

    # 초기의 0 0 c 저장
    while(q):
        x,y = q.popleft()
        z = c - x - y
        if x == 0 :
            answer.append(z)

        # x -> y
        water = min(x, b-y)
        check(x - water, y + water)
        # x -> z
        water = min(x, c-z)
        check(x - water, y)
        # y -> x
        water = min(y, a-x)
        check(x + water, y - water)
        # y -> z
        water = min(y, c-z)
        check(x, y - water)
        # z -> x
        water = min(z, a-x)
        check(x + water, y)
        # z -> y
        water = min(z, b-y)
        check(x, y + water)

visited = [[False] * (b+1) for _ in range(a+1)]
visited[0][0] = True
answer = []
q = deque()
q.append((0, 0))
bfs()
answer.sort()
for i in answer:
    print(i, end=" ")