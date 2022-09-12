#https://www.acmicpc.net/problem/1463

n = int(input())
arr = [-1]*1000001

arr[1] = 0
arr[2] = 1
arr[3] = 1

if n>3:
    for i in range(4, n+1):
        arr[i] = arr[i-1]+1
        if i%3 == 0:
            arr[i] = min(arr[i], arr[i//3]+1)
        if i%2 == 0:
            arr[i] = min(arr[i], arr[i//2]+1)

print(arr[n])