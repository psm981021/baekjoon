#https://www.acmicpc.net/problem/1676

import math
num =int(input())
num=math.factorial(num)
cnt =0

for i in reversed(str(num)):
    if(i == '0'):
        cnt+=1
    else:
        print(cnt);break
