#https://www.acmicpc.net/problem/2022

import math
x,y,c = map(float, input().split())

#제곱으로 오차 -6
allow = 10e-6

right = min(x,y)
left = 1
ans = 0

while abs(right - left) >= allow :

    mid = (right + left) /2
    h1 = (x ** 2 - mid ** 2) ** 0.5
    h2 = (y ** 2 - mid ** 2) ** 0.5

    tmp_c = (h1*h2)/(h1+h2)
    if tmp_c >= c:
        ans = mid
        left = mid
    else:
        right = mid

print("{}".format(round(ans, 4)))