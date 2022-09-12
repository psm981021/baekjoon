#https://www.acmicpc.net/problem/1764


n,m = map(int,input().split())

a=[]
b=[]
result=[]

for i in range(n):
    a.append(str(input()))
for i in range(m):
    b.append(str(input()))    
a=set(a)
b=set(b)
result = a.intersection(b)

result =sorted(result)
print(len(result))
for i in result:
    print(i)