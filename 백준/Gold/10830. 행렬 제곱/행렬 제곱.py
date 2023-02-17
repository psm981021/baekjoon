
#https://www.acmicpc.net/problem/10830

n, b = map(int, input().split())
A = [list(map(int,input().split())) for _ in range(n)]
p = 1000

def cal(A,B):
    n=len(A[0])
    C=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for l in range(n):
                C[i][j]+=A[i][l]*B[l][j]%p
    return C

def square(n,k):

    if k==1:
        return n
    tmp=square(n,k//2)
    if k%2==0:
        return cal(tmp,tmp)
    else:
        return cal(cal(tmp,tmp),n)

result=square(A,b)

for i in range(n):
    for j in range(n):
        print(result[i][j]%p,end=' ')
    print()