#https://www.acmicpc.net/problem/14225


import sys
from itertools import combinations
from collections import Counter


a,b,c = (map(int,sys.stdin.readline().split()))

def pow_n(a,b):
    if(b==1):
        return a%c
    elif(b%2==0):
        num = pow_n(a,b//2)
        return num*num%c
    else:
        num = pow_n(a,(b-1)//2)
        return num*num*a%c

print(pow_n(a,b))