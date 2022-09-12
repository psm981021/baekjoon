import sys
from collections import deque



#https://www.acmicpc.net/problem/10828

n = int(sys.stdin.readline())
stack = deque()
for _ in range(n):
    com = list(map(str,sys.stdin.readline().split()))

    if 'push' in com:
        com, num = com[0], int(com[1])
        stack.appendleft(num)

    elif 'pop' in com:
        com = com[0]
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.popleft())


    elif 'top' in com:
        com = com[0]
        if len(stack) == 0:
            print(-1)
        else:
            tmp =stack.popleft()
            stack.appendleft(tmp)
            print(tmp)

    elif 'size' in com:
        com = com[0]
        print(len(stack))

    elif 'empty' in com:
        com = com[0]
        if len(stack) == 0:
            print(1)
        else:
            print(0)