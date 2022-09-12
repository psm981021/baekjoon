import sys
from collections import deque



#https://www.acmicpc.net/problem/1874

n = int(sys.stdin.readline().rstrip())


seq =[]
for _ in range(n):
    seq.append(int(sys.stdin.readline().rstrip()))

number = deque([i for i in range(1, max(seq) + 1)])
stack = deque()
result = []
i = 0
flag = 0
while number or stack:
    if flag == 1:
        break
    if len(number) != 0:
        tmp = number.popleft()
        stack.appendleft(tmp)
        result.append('+')

    if tmp == seq[i]:
        stack.popleft()
        result.append('-')
        i += 1
        while stack:
            tmp = stack.popleft()
            if tmp == seq[i]:
                result.append('-')
                i += 1
            elif tmp > seq[i]:
                print('NO')
                flag = 1
                result.clear()
                break

            else:
                stack.appendleft(tmp)
                break

for _ in range(len(result)):
    print(result[_])