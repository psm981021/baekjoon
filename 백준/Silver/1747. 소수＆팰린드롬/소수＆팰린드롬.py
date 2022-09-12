#https://www.acmicpc.net/problem/1747


import sys
n = 1004000
a = [True] * (n + 1)
m = int(n**0.5)

num = int(sys.stdin.readline())

def palindrome(number):
    number = str(number)
    if(number == number[::-1]):
        return 1
    else:
        return 0
a[1] = False
for i in range(2, m + 1):
    if a[i] == True:
        for j in range(i + i, n + 1, i):
            a[j] = False
#print([i for i in range(num,n+1) if a[i] == True])
for i in range(num,n+1):
    if(a[i] == True):
        if(palindrome(i) == 1):
            print(i)
            break
