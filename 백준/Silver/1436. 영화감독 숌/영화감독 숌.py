#https://www.acmicpc.net/problem/1436


import sys

N = int(sys.stdin.readline())

num = 665
count = 0

while(True):
    if count == N:
        print(num)
        break

    num+=1
    movie = list(str(num))
    for i in range(len(movie)-2):
        if ''.join(movie[i:i+3]) == '666':
            count+=1
            break


