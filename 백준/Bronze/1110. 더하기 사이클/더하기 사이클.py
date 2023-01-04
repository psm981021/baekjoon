#https://www.acmicpc.net/problem/1110

import sys

N = str(sys.stdin.readline().rstrip())

cnt =  0

#새로운 숫자
tmp = -1
new_num = -1

#flag
M = int(N)

# 초기 숫자가 한자리 수 일대
if int(N) < 10:
    N = '0'+N

while new_num != M :
    cnt+=1

    tmp = int(N[0]) + int(N[1])
    new_num = int(N[1]) * 10 + tmp % 10
    N = str(new_num)

    #결과가 한자리 수 일때
    if len(N) == 1 :
        N = '0'+N

print(cnt)



