#https://www.acmicpc.net/problem/13458

import sys
N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B,C = map(int, (sys.stdin.readline().split()))

director = N

for _ in A:
    #응시생 수가 B보다 작을 때
    if _ - B <= 0 :
        continue
    else:
        if _ - B <= C:
            director += 1
        elif (_ - B) % C == 0 :
            director += ( _ -B)// C
        else :
            director += (_ - B  ) // C  +1
print(director)