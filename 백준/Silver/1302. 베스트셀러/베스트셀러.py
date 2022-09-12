#https://www.acmicpc.net/problem/1302

n = int(input())
result ={}

for i in range(n):
    st = str(input())
    if(st not in result):
        result[st]= 1
    else:
        result[st]+=1
result =sorted(result.items())


print((max(result, key = lambda result: result[1]))[0])