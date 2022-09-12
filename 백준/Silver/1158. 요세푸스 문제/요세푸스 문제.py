#https://www.acmicpc.net/problem/1158

n,k = map(int,input().split())
yos = [i for i in range(1,n+1)]
result =[]

cnt = 0;l = len(yos)

while(True):
    l = len(yos)
    if(l ==0):
        break
    if(len(yos) <4):
        cnt+=k-1
        while(cnt >= l):
            cnt = cnt-l
            
        result.append(yos[cnt])
        del[yos[cnt]]
    else:
        cnt+=k-1
        while(cnt >= l):
            cnt = cnt-l
        result.append(yos[cnt])
        del[yos[cnt]]
print("<" + ", ".join(list(map(str, result))) + ">")